from rest_framework import serializers

from app.models import TestData


class TestDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestData
        fields = ('id', 'unit_number', 'time_cycles')

