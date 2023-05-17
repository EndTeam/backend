from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product, ProductColor, Size, Color, Brand, Category, ProductUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductUser
        fields = '__all__'


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
    is_favorite = serializers.BooleanField(default=False)
    class Meta:
        model = Product
        fields = ['id', "name", "article", "cost", "sale_cost", "new", "sale", "description", "image_color", "size",
                  "brand", "category", 'is_favorite']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
