from django.urls import path
from .views import *

urlpatterns = [
    path('products/popular/', Popular_Products),
    path('get-info/', Get_Info),
    path('products/all/', Products_All),
    path('get-slider/', Get_Slider),
    path('get-slider/', Get_Slider),
]
