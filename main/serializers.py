from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product, ProductColor, Size, Color, Brand, Category, ProductUser, Basket, Order, OrderPiece, \
    MainCategory, Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff",
                  "is_active", "date_joined", "groups", "user_permissions"]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MainCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = MainCategory
        fields = ['id', 'main_category', 'category', 'image']


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


class ProductBasketSerializer(serializers.ModelSerializer):
    image_color = ProductColorSerializer(source='productcolor_set', many=True)
    size = SizeSerializer(many=True)
    brand = BrandSerializer()
    category = CategorySerializer()
    is_favorite = serializers.BooleanField(default=False)

    class Meta:
        model = Product
        fields = ['id', "name", "article", "cost", "sale_cost", "new", "sale", "description", "image_color", "size",
                  "brand", "category", 'is_favorite']


class BasketSerializer(serializers.ModelSerializer):
    # product = ProductBasketSerializer()
    # color = ColorSerializer()
    # size = SizeSerializer()

    class Meta:
        model = Basket
        fields = '__all__'


class OrderPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPiece
        fields = '__all__'


class OrderPieceTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPiece
        fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    order_piece = OrderPieceSerializer(many=True, source='orderpiece_set')

    class Meta:
        model = Order
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


from django.contrib.auth import authenticate

from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs
