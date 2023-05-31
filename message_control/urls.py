from django.urls import path, include
from .views import MessageViewSet, MatchExViewSet, ChatRoomViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('messages', MessageViewSet, basename='messages')
router.register('matchings', MatchExViewSet, basename='matchings')
router.register('chatrooms', ChatRoomViewSet, basename='chatrooms')


urlpatterns = [
    path('', include(router.urls)),
]

