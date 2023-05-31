from django.urls import path, include
from .views import (
    LinkViewSet,
    GooglesheetsViewSet, 
    GsViewSet, 
    DiagViewSet,
    SurViewSet,
    PerioViewSet,
    OperViewSet,
    PedoViewSet,
    EndoViewSet,
    ProsthViewSet)

from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView


router = DefaultRouter()
router.register('links', LinkViewSet, basename='links')
router.register('googlesheets', GooglesheetsViewSet, basename='googlesheets')
router.register('gs', GsViewSet, basename='gs')
router.register('diags', DiagViewSet, basename='diags')
router.register('surs', SurViewSet, basename='surs')
router.register('perios', PerioViewSet, basename='perios')
router.register('opers', OperViewSet, basename='opers')
router.register('pedos', PedoViewSet, basename='pedos')
router.register('endos', EndoViewSet, basename='endos')
router.register('prosths', ProsthViewSet, basename='prosths')

urlpatterns = [
    path('', include(router.urls)),

]

