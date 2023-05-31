from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role


class BotConfig(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)  # 'text' or 'voice'
    # any other relevant data

    def __str__(self):
        return self.name