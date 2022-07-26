# Generated by Django 4.0.5 on 2022-07-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
            ],
        ),
    ]
