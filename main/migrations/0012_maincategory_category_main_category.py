# Generated by Django 4.2.1 on 2023-06-02 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_order_orderpiece_order_order_piece_order_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.TextField(max_length=20, verbose_name='основная_категория')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='main.maincategory'),
        ),
    ]
