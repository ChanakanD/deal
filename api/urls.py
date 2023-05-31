from django.urls import path, include
from .views import UserViewSet, NotificationViewSet

from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('notifications', NotificationViewSet, basename='notifications')
# router.register('chats', ChatViewSet, basename='chats')
# router.register('messages', MessageViewSet, basename='messages')
# router.register('matchuser', MatchUserViewSet, basename='matchuser')

urlpatterns = [
    path('', include(router.urls)),

]

