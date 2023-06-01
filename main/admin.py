from django.contrib import admin
from .models import Product, Size, Color, ProductColor, Brand, Category, ProductUser, Basket, Order, OrderPiece

# Register your models here.


admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductUser)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(OrderPiece)
