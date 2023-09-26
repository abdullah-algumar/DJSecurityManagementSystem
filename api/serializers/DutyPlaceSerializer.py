from rest_framework import serializers
from api.models import DutyPlace

class DutyPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyPlace
        fields = '__all__'