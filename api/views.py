from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view


def Slider(request):
    slider = Slider.objects.all()
    