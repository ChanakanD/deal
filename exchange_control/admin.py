from django.contrib import admin
from .models import Exchange, DateTime, SelectedEx, Central, SelectedCent

# admin.site.register(Exchange)
@admin.register(Exchange)
class ExchangeModel(admin.ModelAdmin):
    list_filter = ('category', 'status')
    list_display = ('id', 'category', 'case_have', 'case_want', 'option', 'task', 'status', 'case_match')

@admin.register(DateTime)
class DateTimeModel(admin.ModelAdmin):
    list_display = ('value', 'check', 'am', 'pm')

@admin.register(SelectedEx)
class SelectedExModel(admin.ModelAdmin):
    list_display = ('id', 'caseEx', 'user')

@admin.register(Central)
class CentralModel(admin.ModelAdmin):
    list_filter = ('case',)
    list_display = ('id', 'no', 'case', 'author', 'timeout', 'post')

@admin.register(SelectedCent)
class SelectedCentModel(admin.ModelAdmin):
    list_display = ('central', 'user')

