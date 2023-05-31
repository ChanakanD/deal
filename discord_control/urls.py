from django.urls import path, include
from .views import RolelViewSet, BotConfigViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('roles', RolelViewSet, basename='roles')
router.register('bots', BotConfigViewSet, basename='bots')



urlpatterns = [
    path('', include(router.urls)),

]