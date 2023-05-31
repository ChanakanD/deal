from rest_framework import serializers
from .models import User, Notification
# from googleSheets_control.serializers import GooglesheetsSerializer
# from message_control.serializers import MessageSerializer



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        # fields = ('id', 'username', 'first_name', 'last_name', 'pic', 'lastLogin', 'role', 'group', 'friends', 'message_sender')


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    author = UserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Notification
        fields = "__all__"

