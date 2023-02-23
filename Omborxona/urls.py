from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats/', include('statsapp.urls')),
    path('', include('userapp.urls')),
    path('bolim/', include('asosiy.urls')),




]
