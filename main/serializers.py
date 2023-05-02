from rest_framework import serializers
from .models import Product, ProductColor, Size, Color, Brand, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ProductColorSerializer(serializers.ModelSerializer):
    img_name = serializers.ReadOnlyField(source='product.name')
    color = ColorSerializer()
    class Meta:
        model = ProductColor
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image_color = ProductColorSerializer(source='productcolor_set', many=True)
    size = SizeSerializer(many=True)
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'
