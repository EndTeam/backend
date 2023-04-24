from django.db import models

# Create your models here.


class Size(models.Model):
    size = models.IntegerField('Размер', )


class Color(models.Model):
    name = models.TextField('Цвет', max_length=20)


class Brand(models.Model):
    name = models.TextField('Бренд', max_length=20)


class Product(models.Model):
    name = models.TextField('Название', max_length=20)
    article = models.TextField('Артикул', max_length=20)
    cost = models.FloatField('Цена',)
    sale_cost = models.FloatField('Скидочная_цена',)
    new = models.BooleanField('Новый?',)
    sale = models.BooleanField('Скидка?',)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField('Описание')
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)


class Image(models.Model):
    image = models.ImageField('Изображение')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)