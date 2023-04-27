from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class Size(models.Model):
    size = models.IntegerField('Размер', )

    def __str__(self):
        return str(self.size)


class Color(models.Model):
    name = models.TextField('Цвет', max_length=20)
    color = models.BigIntegerField('код (десятичный)', default=4278190080,) #цвет храним как десятеричную версию хеша ARGB
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.TextField('Бренд', max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField('Название', max_length=20)
    article = models.TextField('Артикул', max_length=20)
    cost = models.FloatField('Цена', )
    sale_cost = models.FloatField('Скидочная_цена', )
    new = models.BooleanField('Новый?', )
    sale = models.BooleanField('Скидка?', )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField('Описание')
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color, through='ProductColor')

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    image = models.ImageField('Изображение',upload_to='main/static/main/images')
    name = models.TextField('Название', max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
