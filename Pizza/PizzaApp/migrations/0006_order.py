# Generated by Django 3.2.4 on 2021-07-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0005_cart_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('mnumb', models.CharField(max_length=10)),
                ('pizzas', models.CharField(max_length=10000)),
                ('tcost', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]