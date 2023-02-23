from django.urls import path
from .views import *


urlpatterns = [
    path('', StatsView.as_view(), name='stats'),
    path('stats_edit/<int:pk>/', StatsEditView.as_view(), name='stats_edit')
]