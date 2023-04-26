# Generated by Django 3.1.2 on 2023-04-26 02:34

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.TextField(default=2, max_length=20, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
