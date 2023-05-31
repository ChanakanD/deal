from django.shortcuts import render
from .models import Exchange, DateTime, SelectedEx, Central, SelectedCent
from .serializers import ExchangeSerializer, DateTimeSerializer, SelectedExSerializer, CentralSerializer, SelectedCentSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class DateTimeViewSet(viewsets.ModelViewSet):
    queryset = DateTime.objects.all()
    serializer_class = DateTimeSerializer

class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

class SelectedExViewSet(viewsets.ModelViewSet):
    queryset = SelectedEx.objects.all()
    serializer_class = SelectedExSerializer
    
class CentralViewSet(viewsets.ModelViewSet):
    queryset = Central.objects.all()
    serializer_class = CentralSerializer

class SeletedCentViewSet(viewsets.ModelViewSet):
    queryset = SelectedCent.objects.all()
    serializer_class = SelectedCentSerializer