from rest_framework import serializers
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
# from api.serializers import UserSerializer

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

class GooglesheetsSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Googlesheets
        fields = "__all__"

class GSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gs
        fields = "__all__"

class DiagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diag
        fields = "__all__"

class SurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sur
        fields = "__all__"

class PerioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perio
        fields = "__all__"

class OperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oper
        fields = "__all__"

class PedoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedo
        fields = "__all__"

class EndoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endo
        fields = "__all__"

class ProsthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prosth
        fields = "__all__"
      