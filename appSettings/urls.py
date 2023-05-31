from django.urls import path, include
from .views import SettingsView

from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

router = DefaultRouter()
# router.register('settings', SettingsView, basename='settings')


urlpatterns = [
    # path('appSetting/', include(router.urls)),
    path('settings', SettingsView.as_view(),),
    path('create-new-setting/', SettingsView.as_view(),)

]

