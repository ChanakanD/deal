from rest_framework import serializers
from .models import Role, BotConfig


class RoleSerializer(serializers.ModelSerializer):
    # role = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Role
        fields = ('id', 'role')


class BotConfigSerializer(serializers.ModelSerializer):
    name = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = BotConfig
        fields = '__all__'