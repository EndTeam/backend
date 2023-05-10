from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
from main.models import Product, ProductColor, Brand, Size, Color, Category
from main.pagination import StandardResultsSetPagination
from main.serializers import ProductSerializer, BrandSerializer, SizeSerializer, ColorSerializer, \
    ProductColorSerializer, CategorySerializer
from rest_framework import viewsets


# Create your views here.


def main(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')


class ProductAPI(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({'products': ProductSerializer(products, many=True).data})

    def post(self, request):
        return Response()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['name']
    filterset_fields = ["brand", "size", 'color', 'category']
    pagination_class = StandardResultsSetPagination


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class PictureViewSet(viewsets.ModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
