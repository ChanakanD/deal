from django.db import models
from api.models import User


class Exchange(models.Model):
    category = models.CharField(max_length=10)
    case_have = models.CharField(max_length=10, null=True, blank=True)
    case_want = models.CharField(max_length=10, null=True, blank=True)
    option = models.CharField(max_length=10, null=True, blank=True)
    task = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    start_date = models.CharField(max_length=10)
    stop_date = models.CharField(max_length=10)
    detail = models.TextField()
    status = models.CharField(max_length=10)
    author = models.ForeignKey(User, related_name="exchange", on_delete=models.CASCADE)
    case_match = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
    # user_match = models.ForeignKey(User, related_name="user_match", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.category}"


class DateTime(models.Model):
    exchange = models.ForeignKey(Exchange, related_name="date_time", on_delete=models.CASCADE)
    label = models.CharField(max_length=2)
    value = models.CharField(max_length=2)
    checked = models.BooleanField(default=False)
    am = models.BooleanField(default=False)
    pm = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.value} {self.am} - {self.pm}"


class SelectedEx(models.Model):
    caseEx = models.ForeignKey('Exchange', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ex_case: {self.caseEx.id} is {self.user.id} selected"


class Central(models.Model):
    no = models.CharField(max_length=5)
    case = models.CharField(max_length=10)
    option = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    timestamp_out = models.DateTimeField(null=True, blank=True)
    timeout = models.BooleanField(default=False)
    post = models.BooleanField(default=False)
    admin = models.ForeignKey(User, related_name="central_admin", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="central_user", on_delete=models.CASCADE)
    selects = models.ManyToManyField(User, related_name="cent_selects", through='SelectedCent')

    def __str__(self):
        return self.no


class SelectedCent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    central = models.ForeignKey('Central', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"User: {self.user.username} selected Cent no. {self.central.no}"