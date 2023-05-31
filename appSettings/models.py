from django.db import models

class Setting(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False, default="settings_name")
    value = models.CharField(max_length=256, blank=False, null=False, default='')
    