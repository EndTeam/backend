# Generated by Django 4.2.1 on 2023-05-22 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_productuser_product_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(related_name='product_favorite', through='main.ProductUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('product', 'user', 'color', 'size')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='basket_piece',
            field=models.ManyToManyField(related_name='product_basket', through='main.Basket', to=settings.AUTH_USER_MODEL),
        ),
    ]
