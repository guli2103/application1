from django.db import models

class Moshin(models.Model):
    firmasi = models.CharField(max_length=20)
    nomi = models.CharField(max_length=20)
    rangi = models.TextField()
    yili = models.IntegerField(default=2000)

class Kopmyuter(models.Model):
    kompaniyasi =models.CharField(max_length=20)
    rangi = models.CharField(max_length=20)
    protsessori = models.IntegerField(default=4)
    xotirasi = models.IntegerField(default=8)

class Telefon(models.Model):
    kompaniyasi = models.CharField(max_length=20)
    rangi = models.CharField(max_length=20)
    xotirasi = models.IntegerField(default=32)
    kamerasi= models.IntegerField(default=2)  

