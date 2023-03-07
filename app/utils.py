from django.db.models import Max, Min


def fixed4(num):
    return round(float(num), 4)

def getMaxMin(model, column):
    return {
        "max": fixed4(model.objects.aggregate(Max(column))[f"{column}__max"]),
        "min": fixed4(model.objects.aggregate(Min(column))[f"{column}__min"]),
    }