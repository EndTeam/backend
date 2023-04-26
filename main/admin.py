from django.contrib import admin
from .models import Product, Size, Color, ProductColor, Brand
# Register your models here.

admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(Brand)