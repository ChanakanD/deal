from django.shortcuts import render
from .models import User, Notification
from .serializers import UserSerializer,  NotificationSerializer
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework import viewsets
# from django.shortcuts import get_object_or_404
from google.oauth2 import service_account
from googleapiclient.discovery import build


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


