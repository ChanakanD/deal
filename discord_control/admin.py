from django.contrib import admin
from .models import Role, BotConfig

@admin.register(Role)
class RoleModel(admin.ModelAdmin):
    list_display = ('id', 'role')

@admin.register(BotConfig)
class BotConfigModel(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'category')
