from django.contrib import admin
from .models import Message, MatchEX, ChatRoom

@admin.register(Message)
class MessageModel(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'is_read')
    # list_display = ('content', 'updated_at')


@admin.register(MatchEX)
class MatchEXModel(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(ChatRoom)
class ChatRoomModel(admin.ModelAdmin):
    list_display = ('lastMessage', 'newMessages')


