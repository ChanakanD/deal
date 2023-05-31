from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/user/', include('api.urls')),
    path('api/v1.0/app/', include('appSettings.urls')),
    path('api/v1.0/case/', include('exchange_control.urls')),
    path('api/v1.0/message/', include('message_control.urls')),
    path('api/v1.0/googlesheets/', include('googleSheets_control.urls')),
    path('api/v1.0/discord/', include('discord_control.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)