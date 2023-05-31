from django.shortcuts import render
from .models import (
    Link,
    Googlesheets, 
    Gs, 
    Diag,
    Sur, 
    Perio, 
    Oper, 
    Pedo, 
    Endo, 
    Prosth)
from .serializers import (
    LinkSerializer,
    GooglesheetsSerializer, 
    GSSerializer, 
    DiagSerializer,
    SurSerializer,
    PerioSerializer,
    OperSerializer,
    PedoSerializer,
    EndoSerializer,
    ProsthSerializer)

from rest_framework import viewsets

# import gspread
from django.core.management import call_command
from google.oauth2 import service_account

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class GooglesheetsViewSet(viewsets.ModelViewSet):
    queryset = Googlesheets.objects.all()
    serializer_class = GooglesheetsSerializer

class GsViewSet(viewsets.ModelViewSet):
    queryset = Gs.objects.all()
    serializer_class = GSSerializer

class DiagViewSet(viewsets.ModelViewSet):
    queryset = Diag.objects.all()
    serializer_class = DiagSerializer

class SurViewSet(viewsets.ModelViewSet):
    queryset = Sur.objects.all()
    serializer_class = SurSerializer

class PerioViewSet(viewsets.ModelViewSet):
    queryset = Perio.objects.all()
    serializer_class = PerioSerializer

class OperViewSet(viewsets.ModelViewSet):
    queryset = Oper.objects.all()
    serializer_class = OperSerializer

class PedoViewSet(viewsets.ModelViewSet):
    queryset = Pedo.objects.all()
    serializer_class = PedoSerializer

class EndoViewSet(viewsets.ModelViewSet):
    queryset = Endo.objects.all()
    serializer_class = EndoSerializer

class ProsthViewSet(viewsets.ModelViewSet):
    queryset = Prosth.objects.all()
    serializer_class = ProsthSerializer

