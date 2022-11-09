# Generated by Django 4.1.3 on 2022-11-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moshin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kopmyuter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kompaniyasi', models.CharField(max_length=20)),
                ('rangi', models.CharField(max_length=20)),
                ('protsessori', models.IntegerField(default=4)),
                ('xotirasi', models.IntegerField(default=8)),
            ],
        ),
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kompaniyasi', models.CharField(max_length=20)),
                ('rangi', models.CharField(max_length=20)),
                ('xotirasi', models.IntegerField(default=32)),
                ('kamerasi', models.IntegerField(default=2)),
            ],
        ),
    ]