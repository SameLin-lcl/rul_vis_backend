import json

from django.core import serializers
from django.db import connection
from django.db.models import Max, Min, Q
from django.http import JsonResponse
from app.models import TestUnitPca, ModelScores, TestInstances, ShapValue, InstanceHi, RulLoss
from app.utils import getMaxMin, fixed4
import numpy as np
from django.db.models import F, Avg

rdx, rdy = "umap_x", "umap_y"
rdx_unit, rdy_unit = "umap_x", "umap_y"


def queryUnitsPca(request):
    rul = json.loads(request.GET.get('rul') or 'null')
    if rul is None:
        queryset = TestUnitPca.objects.all()
    else:
        queryset = TestUnitPca.objects.filter(
            Q(rul__gte=rul[0]) & Q(rul__lte=rul[1])
        )
    data = {
        "maxMin": {
            "x": getMaxMin(TestUnitPca, rdx_unit),
            "y": getMaxMin(TestUnitPca, rdy_unit),
            "rul": getMaxMin(TestUnitPca, "rul"),
        }, "units": []
        # json.dumps(
        #     TestUnitPca.objects.all().values('unit_number', 'x', 'y', 'rul').annotate(
        #         unitId=F('unit_number'),
        #     ).values('unitId', 'x', 'y', 'rul'))
    }
    for res in queryset:
        data["units"].append({
            "unitId": res.unit_number,
            "x": getattr(res, rdx_unit),
            "y": getattr(res, rdy_unit),
            "rul": res.rul
        })
    return JsonResponse({"data": data})


def queryModelScore(request):
    queryset = ModelScores.objects.exclude(model__in=['BAYES','LSTM1', 'GRU'])
    loss_queryset = RulLoss.objects.all()

    score_columns = ["score", "rsme", "r2"]

    with connection.cursor() as cursor:
        cursor.execute('SELECT MAX(score), MAX(RSME), MAX(R2) FROM model_scores where model != "BAYES"')
        row = cursor.fetchone()

    data = {
        "maxMin": {
            "perf": [{"label": col, "max": row[idx]} for idx, col in
                     enumerate(score_columns)],
            "deviation": {
                "max": -float("inf"),
                "min": float("inf")
            },
            "variance": {
                "max": -float("inf"),
                "min": float("inf")
            }
        },
        "models": []
    }

    # for perf in score_columns:
    #     data["maxMin"]["perf"].append({
    #         "label": perf,
    #         "max": fixed4(ModelScores.objects.aggregate(Max(perf))[f"{perf}__max"]),
    #     })

    models = list(queryset.values_list('model', flat=True).distinct())
    deviation_dict = {x: [] for x in models}

    for left, right in [[0, 40], [40, 90], [90, 140], [140, 200], [200, 311]]:
        print(left, right)
        res = loss_queryset[left: right]
        for m in models:
            mean = sum([abs(getattr(r, f'{m.lower()}_mean')) for r in res]) / (right - left)
            std = [getattr(r, f'{m.lower()}_std') for r in res if getattr(r, f'{m.lower()}_std') != 0]
            std = sum(std) / len(std)
            mean, std = fixed4(mean), fixed4(std)
            data["maxMin"]["deviation"]["max"] = max(data["maxMin"]["deviation"]["max"], mean)
            data["maxMin"]["deviation"]["min"] = min(data["maxMin"]["deviation"]["min"], mean)
            data["maxMin"]["variance"]["max"] = max(data["maxMin"]["variance"]["max"], std)
            data["maxMin"]["variance"]["min"] = min(data["maxMin"]["variance"]["min"], std)
            deviation_dict[m].insert(0, {
                "label": f'{left} - {right}',
                "value": mean,
                "variance": std
            })

    for res in queryset:
        data["models"].append({
            "model": res.model,
            "perf": [{"label": col, "value": fixed4(res.__dict__[col])} for col in score_columns],
            "deviation": deviation_dict[res.model]
        })

    return JsonResponse({"data": data})


def queryInputData(request):
    units = json.loads(request.GET.get('units') or 'null')
    models = json.loads(request.GET.get('models') or 'null')
    rul_range = json.loads(request.GET.get('rulRange') or 'null')
    win = int(request.GET.get('win') or 1)

    if units is None:
        queryset = TestInstances.objects.filter(
            Q(rul__gte=rul_range[0]) & Q(rul__lte=rul_range[1])
        )
    else:
        queryset = TestInstances.objects.filter(unit_number__in=units).filter(
            Q(rul__gte=rul_range[0]) & Q(rul__lte=rul_range[1])
        )

    model_loss = [x for x in dir(TestInstances) if x.endswith("_loss")]

    if models:
        model_loss = [f'{x.lower()}_loss' for x in models if f'{x.lower()}_loss' in model_loss]

    features = sorted([x for x in dir(TestInstances) if x.startswith("s_")], key=lambda x: int(x[2:]))

    max_rul_queryset = TestInstances.objects.values("unit_number").annotate(Max('rul'))

    max_rul = {}
    for row in max_rul_queryset:
        max_rul[row['unit_number']] = row['rul__max']

    data = {
        "maxMin": {
            "x": {
                "max": fixed4(queryset.aggregate(Max(rdx))[f"{rdx}__max"] or 0),
                "min": fixed4(queryset.aggregate(Min(rdx))[f"{rdx}__min"] or 0)
            },
            "y": {
                "max": fixed4(queryset.aggregate(Max(rdy))[f"{rdy}__max"] or 0),
                "min": fixed4(queryset.aggregate(Min(rdy))[f"{rdy}__min"] or 0)
            },
            # "features": {
            #     "max": fixed4(max([x or 0 for x in queryset.aggregate(*[Max(x) for x in features]).values()])),
            #     "min": fixed4(min([x or 0 for x in queryset.aggregate(*[Min(x) for x in features]).values()]))
            # },
            "modelPerf": {
                "max": fixed4(
                    max([x or 0 for x in TestInstances.objects.aggregate(*[Max(x) for x in model_loss]).values()])),
                "min": fixed4(
                    min([x or 0 for x in TestInstances.objects.aggregate(*[Min(x) for x in model_loss]).values()]))
            }
        },
        "instances": []
    }

    last_unit_number = 0

    for res in queryset:
        if res.unit_number != last_unit_number:
            counter = 0
            last_unit_number = res.unit_number
        if counter % win == 0:
            data["instances"].append({
                "instanceId": res.input_id,
                "unitId": res.unit_number,
                "x": fixed4(getattr(res, rdx)),
                "y": fixed4(getattr(res, rdy)),
                "rul": res.rul,
                "rulMax": max_rul[res.unit_number],
                "modelPerf": [{"label": m.upper()[:-5], "value": fixed4(getattr(res, m))} for m in model_loss]
            })
        counter = counter + 1
    return JsonResponse({"data": data})


def queryInstanceFeatures(request):
    instances = json.loads(request.GET.get('instances') or 'null')
    models = json.loads(request.GET.get('models') or 'null')

    features = sorted([x for x in dir(TestInstances) if x.startswith("s_")], key=lambda x: int(x[2:]))
    model_shaps = {model: [f'{model.lower()}_{feature}' for feature in features] for model in models}

    inputQueryset = TestInstances.objects.filter(input_id__in=instances)
    shapQueryset = ShapValue.objects.filter(input_id__in=instances)

    max_rul = {}
    for row in TestInstances.objects.values("unit_number").annotate(Max('rul')):
        max_rul[row['unit_number']] = row['rul__max']

    data = {
        "maxMin": {
            "importance": {
                "max": fixed4(max([x or 0 for x in shapQueryset.aggregate(
                    *[Max(x) for x in np.array(list(model_shaps.values())).flatten() if x in dir(ShapValue)]).values()])),
                "min": fixed4(min([x or 0 for x in shapQueryset.aggregate(
                    *[Min(x) for x in np.array(list(model_shaps.values())).flatten() if x in dir(ShapValue)]).values()]))
            },
            "meanAbsImportance": [],
            "maxAbsImportance": []
        },
        "features": [{
            "name": f,
            "max": fixed4(TestInstances.objects.aggregate(Max(f))[f"{f}__max"]),
            "min": fixed4(TestInstances.objects.aggregate(Min(f))[f"{f}__min"]),
            "overImportance": [{
                "label": m,
                "importance": fixed4(shapQueryset.aggregate(Avg(f'{m.lower()}_{f}'))[f'{m.lower()}_{f}__avg']) if f'{m.lower()}_{f}' in dir(ShapValue) else 0
            } for m in models]
        } for f in features
        ],
        "instances": []
    }

    for input, shap in zip(inputQueryset, shapQueryset):
        data["instances"].append({
            "instanceId": input.input_id,
            "unitId": input.unit_number,
            "rul": input.rul,
            "rulMax": max_rul[input.unit_number],
            "modelPerf": [{"label": m, "value": fixed4(getattr(input, f'{m.lower()}_loss'))} for m in models],
            "features": [{
                "label": f,
                "value": fixed4(getattr(input, f)),
                "importance": (value := [{
                    "label": m,
                    "value": fixed4(getattr(shap, f'{m.lower()}_{f}', 0))
                } for m in models]),
                "meanAbsImportance": fixed4(sum([abs(x["value"]) for x in value]) / len(value))
            } for f in features]
        })

    absImportance = [
        [instance["features"][i]["meanAbsImportance"] for instance in data["instances"]] for i, f in enumerate(features)
    ]

    data["maxMin"]["meanAbsImportance"] = [fixed4(sum(x) / len(data)) for x in absImportance]
    data["maxMin"]["maxAbsImportance"] = [max(x) for x in absImportance]

    return JsonResponse({"data": data})


def queryInstanceTimeline(request):
    input = request.GET.get('input')
    models = json.loads(request.GET.get('models') or 'null')

    unit_number = TestInstances.objects.get(input_id=input).unit_number

    features = sorted([x for x in dir(TestInstances) if x.startswith("s_")], key=lambda x: int(x[2:]))
    model_shaps = {model: [f'{model.lower()}_{feature}' for feature in features] for model in models}

    model_loss = [x for x in dir(TestInstances) if x.endswith("_loss") and x[:-5].upper() in models]

    inputQueryset = TestInstances.objects.filter(unit_number=unit_number)
    input_ids = [row.input_id for row in inputQueryset]
    shapQueryset = ShapValue.objects.filter(input_id__in=input_ids)
    hiQueryset = InstanceHi.objects.filter(input_id__in=input_ids)

    print("SAMELIN## ", model_shaps)
    rul_loss_dict = {getattr(row, "rul"): {
        f'{m}': {"mean": getattr(row, f'{m.lower()}_mean'), "std": getattr(row, f'{m.lower()}_std')} for m in models
    } for row in RulLoss.objects.all()}

    data = {
        "info": {
            "unit": unit_number,
            "timeline": inputQueryset.aggregate(Max("rul"))["rul__max"] + 1
        },
        "maxMin": {
            "hi": {
                "max": 1,
                "min": 0
            },
            "pred": {
                "max": fixed4(
                    max([x or 0 for x in TestInstances.objects.aggregate(*[Max(x) for x in model_loss]).values()])),
                "min": fixed4(
                    min([x or 0 for x in TestInstances.objects.aggregate(*[Min(x) for x in model_loss]).values()]))
            },
            "importance": {
                "max": fixed4(max([x or 0 for x in shapQueryset.aggregate(
                    *[Max(x) for x in np.array(list(model_shaps.values())).flatten() if x in dir(ShapValue)]).values()])),
                "min": fixed4(min([x or 0 for x in shapQueryset.aggregate(
                    *[Min(x) for x in np.array(list(model_shaps.values())).flatten() if x in dir(ShapValue)]).values()]))
            }
        },
        "overall": [fixed4(row.hi) for row in hiQueryset],
        "features": [{
            "label": f,
            "value": [fixed4(getattr(row, f"hi_{f}")) for row in hiQueryset]
        } for f in features],
        "models": []
    }

    for m in models:
        model_value = []
        for i, (input, shap, hi) in enumerate(zip(inputQueryset, shapQueryset, hiQueryset)):
            model_value.append({
                "rul": input.rul,
                "pred": fixed4(getattr(input, f'{m.lower()}_loss')),
                "importance": [{
                    "label": f,
                    "value": fixed4(getattr(shap, f'{m.lower()}_{f}', 0))
                } for f in features],
                "meanPred": fixed4(rul_loss_dict[input.rul][m]["mean"]),
                "variance": fixed4(rul_loss_dict[input.rul][m]["std"]),
            })
        data["models"].append({
            "label": m,
            "value": model_value
        })

    return JsonResponse({"data": data})
