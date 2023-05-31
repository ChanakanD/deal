from django.db import models
from googleSheets_control.models import Googlesheets


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    lastLogin = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=10)
    group = models.CharField(max_length=10)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.id} - {self.username}"


class Notification(models.Model):
    author = models.ForeignKey(User, related_name="author_noti", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_noti", on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    no_case = models.CharField(max_length=5)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.category
