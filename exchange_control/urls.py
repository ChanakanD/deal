from django.urls import path, include
from .views import ExchangeViewSet, DateTimeViewSet, SelectedExViewSet, CentralViewSet, SeletedCentViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView


router = DefaultRouter()
router.register('exchanges', ExchangeViewSet, basename='exchanges')
router.register('datetimes', DateTimeViewSet, basename='datetimes')
router.register('selected_ex', SelectedExViewSet, basename='selected_ex')
router.register('centrals', CentralViewSet, basename='centrals')
router.register('selected_cent', SeletedCentViewSet, basename='selected_cent')

urlpatterns = [
    path('', include(router.urls)),

]

