from django.shortcuts import render
from rest_framework.decorators import action
from .models import Message, MatchEX, ChatRoom
from .serializers import MessageSerializer, MatchExSerializer, ChatRoomSerializer
from rest_framework import viewsets, status


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MatchExViewSet(viewsets.ModelViewSet):
    queryset = MatchEX.objects.all()
    serializer_class = MatchExSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
