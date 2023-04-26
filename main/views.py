from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product, ProductColor
from main.serializers import ProductSerializer


# Create your views here.


def main(request):
    return render(request,'main/main.html')


def about(request):
    return render(request,'main/about.html')


class ProductAPI(APIView):
    def get(self, request):
        products = Product.objects.all().values()
        color = Product.objects.all()
        return Response({'products': ProductSerializer(color, many=True).data})

    def post(self, request):
        return Response()
