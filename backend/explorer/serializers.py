from explorer.models import OperationalUnit, Oilfield, Well
from rest_framework import serializers


class OperationalUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalUnit
        fields = ["id", "name"]


class OilfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oilfield
        fields = ["id", "name", "operational_unit"]


class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = ["id", "name", "oilfield"]
