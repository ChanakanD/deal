from django.contrib import admin
from .models import (
    Link,
    Googlesheets, 
    Gs, 
    Diag,
    Sur, 
    Perio, 
    Oper, 
    Pedo, 
    Endo, 
    Prosth)

@admin.register(Link)
class LinkModel(admin.ModelAdmin):
    list_display = ('id', 'link',)

@admin.register(Googlesheets)
class GooglesheetsModel(admin.ModelAdmin):
    list_filter = ('subject', 'group',)
    list_display = ('subject', 'group',)

@admin.register(Gs)
class GSModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('no_group', 'first_name', 'last_name')

@admin.register(Diag)
class DiagModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('first_name', 'last_name', 'date_update', 'complete', 'screen')

@admin.register(Sur)
class SurModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('first_name', 'last_name', 'date_update', 'tooth_extraction')

@admin.register(Perio)
class PerioModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('first_name', 'last_name', 'date_update', 'S', 'G', 'P')

@admin.register(Oper)
class OperModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('first_name', 'last_name', 'date_update')

@admin.register(Pedo)
class PedoModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('first_name', 'last_name', 'date_update', 'treatmentPlan_full', 'treatmentPlan_half')

@admin.register(Endo)
class EndoModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('first_name', 'last_name', 'date_update', 'teeth_sum')

@admin.register(Prosth)
class ProsthModel(admin.ModelAdmin):
    # list_filter = ('subject', 'group',)
    list_display = ('first_name', 'last_name', 'date_update')


