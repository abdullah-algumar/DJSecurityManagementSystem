from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.models import DutyPlace, DutyTime, SecurityGuard
from api.serializers.DutyPlaceSerializer import DutyPlaceSerializer
from api.serializers.DutyTimeSerializer import DutyTimeSerializer
from api.serializers.SecurityGuardSerializer import SecurityGuardSerializer
from rest_framework.throttling import AnonRateThrottle


class SecurityGuardViewSet(ModelViewSet):
    queryset = SecurityGuard.objects.all()
    serializer_class = SecurityGuardSerializer
    throttle_classes = [AnonRateThrottle]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DutyTimeViewSet(ModelViewSet):
    queryset = DutyTime.objects.all()
    serializer_class = DutyTimeSerializer
    throttle_classes = [AnonRateThrottle]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecurityGuardDutyTimeListView(generics.ListAPIView):
    serializer_class = DutyTimeSerializer

    def get_queryset(self):
        guard_id = self.kwargs.get('pk')
        return DutyTime.objects.filter(guard_id=guard_id)
    
class DutyPlaceViewSet(ModelViewSet):
    queryset = DutyPlace.objects.all()
    serializer_class = DutyPlaceSerializer
    throttle_classes = [AnonRateThrottle]
