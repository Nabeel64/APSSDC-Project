# Generated by Django 3.2.4 on 2021-07-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0003_pizzas_pcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('psize', models.CharField(max_length=50)),
                ('pcost', models.IntegerField()),
            ],
        ),
    ]
