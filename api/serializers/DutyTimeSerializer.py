from rest_framework import serializers
from api.models import DutyTime

class DutyTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyTime
        fields = '__all__'
        depth = 1