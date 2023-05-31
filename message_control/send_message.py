from django.db.models import Q
from api.models import Notification
from message_control.models import ChatRoom, Message


def send_message(message, validated_data):
    sender = validated_data['sender_id']
    receiver = validated_data['receiver_id']

    print(message.id)
    # add message to ChatRoom
    chat_room = ChatRoom.objects.filter(users__id__exact=sender).filter(users__id__exact=receiver)
    print(chat_room, chat_room[0].id)
    chat = ChatRoom.objects.get(id=chat_room[0].id)
    chat.newMessages += 1
    chat.lastMessage = message
    chat.message.add(message.id)
    chat.save()
    # collect in notification
    Notification.objects.create(user_id=receiver, author_id=sender, category="new message", no_case="-")
    print('create notification')