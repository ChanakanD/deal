from django.db.models import Q
from rest_framework import serializers
from .models import Message, MatchEX, ChatRoom
from api.serializers import UserSerializer
from exchange_control.serializers import ExchangeSerializer
from .send_message import send_message



class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.IntegerField(write_only=True)
    receiver = UserSerializer(read_only=True)
    receiver_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Message
        fields = "__all__"

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        # send message
        send_message(message, validated_data)

        return message

    def update(self, instance, validated_data):
        instance.is_read = validated_data.get('is_read', instance.is_read)
        instance.save()

        id_list = [instance.sender.id, instance.receiver.id]
        id_list2 = [instance.receiver.id, instance.sender.id]
        chat_room = ChatRoom.objects.filter(
            Q(users__id__in=id_list) & Q(users__id__in=id_list2)
        )
        # print(chat_room[0].id)
        chat = ChatRoom.objects.get(id=chat_room[0].id)
        chat.newMessages = 0
        chat.save()
        
        return instance

class MatchExSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MatchEX
        fields = "__all__"


class ChatRoomSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    message = MessageSerializer(many=True)
    lastMessage = MessageSerializer(read_only=True)
    lastMessage_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = ChatRoom
        fields = "__all__"


