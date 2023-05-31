from django.shortcuts import render
from .models import Role, BotConfig
from .serializers import RoleSerializer, BotConfigSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
import discord


class RolelViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        def get_server_id(bot_token):
            client = discord.Client(intents=discord.Intents.default())
            print('Logged in as {0.user}'.format(client))
            
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    print(guild.name)
                    print(guild.id)
                    guild = client.get_guild(guild.id)
                
                    # for role_name in serializer.validated_data['role']:
                    role_name = serializer.validated_data['role']
                    role = await guild.create_role(name=role_name, color=discord.Color.red())
                    print(f'Created role "{role}" with ID {role.id}')
                await client.close()
            
            client.run(bot_token)

        bot_token = 'MTA4Mzk5NDk2NjE4OTE1NDM5NA.GYbrel.IOwZ437sOsqiJWBbfJEbJfKZFpKCQBdLn0PTDg'
        get_server_id(bot_token)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BotConfigViewSet(viewsets.ModelViewSet):
    queryset = BotConfig.objects.all()
    serializer_class = BotConfigSerializer

    # @api_view(['POST'])
    # async def create_channel(self, request):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        category_name = serializer.validated_data['category']
        channel_type = serializer.validated_data['type']

        def get_server_id(bot_token):
            client = discord.Client(intents=discord.Intents.default())
            print('Logged in as {0.user}'.format(client))
            
            @client.event
            async def on_ready():
                for guild in client.guilds:
                    print(guild.name)
                    print(guild.id)
                    guild = client.get_guild(guild.id)

                    category = await guild.create_category(category_name)
                    discord_category_id = str(category.id)
                    category_id = guild.get_channel(category.id)
                    print(f'Created category "{category_name}" with ID {discord_category_id}')
                    
                    for channel_name in serializer.validated_data['name']:
                        if channel_type == 'text':
                            channel = await guild.create_text_channel(channel_name, category=category_id)
                        elif channel_type == 'voice':
                            channel = await guild.create_voice_channel(channel_name, category=category_id)
                        print(f'Created channel "{channel}" with ID {discord_category_id} in category "{category}"')
                await client.close()
            client.run(bot_token)
        
        bot_token = 'MTA4Mzk5NDk2NjE4OTE1NDM5NA.GYbrel.IOwZ437sOsqiJWBbfJEbJfKZFpKCQBdLn0PTDg'
        get_server_id(bot_token)

        return Response(serializer.data, status=status.HTTP_200_OK)


