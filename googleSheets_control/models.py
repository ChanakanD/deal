from django.db import models

class Link(models.Model):
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.link

class Googlesheets(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.CharField(max_length=5)
    subject = models.CharField(max_length=10)
    
    def __str__(self):
        return self.group

class Gs(models.Model):
    id = models.IntegerField(primary_key=True)
    no_group = models.CharField(max_length=5, null=True, blank=True)
    no_table = models.CharField(max_length=5, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    stID = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.no_table


class Diag(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    date_update = models.DateField()
    complete = models.IntegerField(null=True,blank=True)
    screen = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sur(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    date_update = models.DateField()
    tooth_extraction = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Perio(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    date_update = models.DateField()
    S = models.IntegerField(null=True,blank=True)
    G = models.IntegerField(null=True,blank=True)
    P = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Oper(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    date_update = models.DateField()
    class_I = models.IntegerField(null=True,blank=True)
    class_II = models.IntegerField(null=True,blank=True)
    class_III = models.IntegerField(null=True,blank=True)
    class_VI = models.IntegerField(null=True,blank=True)
    class_V = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pedo(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    date_update = models.DateField()
    treatmentPlan_full = models.IntegerField(null=True,blank=True)
    treatmentPlan_half = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Endo(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    date_update = models.DateField()
    teeth_sum = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Prosth(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    date_update = models.DateField()
    fixed_PostCore = models.IntegerField(null=True,blank=True)
    fixed_CB = models.IntegerField(null=True,blank=True)
    removable_APD = models.IntegerField(null=True,blank=True)
    removable_RPD = models.IntegerField(null=True,blank=True)
    double_CD = models.IntegerField(null=True,blank=True)
    single_CD = models.IntegerField(null=True,blank=True)
    contrast_CD = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"