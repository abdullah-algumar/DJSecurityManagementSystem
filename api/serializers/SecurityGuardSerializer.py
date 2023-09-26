from rest_framework import serializers
from api.models import SecurityGuard

class SecurityGuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityGuard
        fields = '__all__'