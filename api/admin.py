from django.contrib import admin
from .models import User, Notification


@admin.register(User)
class UserModel(admin.ModelAdmin):
    # list_filter = ('')
    list_display = ('group', 'username', 'first_name', 'last_name',)


@admin.register(Notification)
class NotificationModel(admin.ModelAdmin):
    # list_filter = ('')
    list_display = ('category', 'no_case', 'is_read',)

