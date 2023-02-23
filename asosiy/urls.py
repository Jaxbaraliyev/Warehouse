from django.urls import path
from .views import *

urlpatterns = [
    path("", BolimView.as_view(), name='bolim'),
    path('mahsulot_edit/<int:pk>/', MahsulotEditView.as_view(), name='mahsulot_edit'),
    path('mahsulotlar/', MahsulotView.as_view(), name='mahsulotlar'),
    path('clients/', ClientView.as_view(), name='clients'),
    path('client/<int:pk>/edit/', ClientEditView.as_view(), name='client_edit'),

]