from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from .serializer import *
from .models import *
from rest_framework.response import Response

@api_view(['GET'])
def Popular_Products(request):
    product = Product.objects.filter(rating=5).order_by('-id')[:20]
    ser = ProductSerializer(product, many=True)

    return Response(ser.data)



@api_view(['GET'])
def Get_Info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info)

    return Response(ser.data)



@api_view(['GET'])
def Products_All(request):
    product = Product.objects.all().order_by('-id')[:100]
    ser = ProductSerializer(product, many=True)

    return Response(ser.data)