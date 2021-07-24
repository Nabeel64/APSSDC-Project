# Generated by Django 3.2.4 on 2021-07-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pregular', models.IntegerField()),
                ('pmedium', models.IntegerField()),
                ('plarge', models.IntegerField()),
                ('pimage', models.ImageField(default='achari_do_pyaza.jpg', upload_to='pizzaimages/')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='userpic',
            field=models.ImageField(default='achari_do_pyaza.jpg', upload_to='profliepics/'),
        ),
    ]
