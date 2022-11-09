from django.db import models

class Institut(models.Model):
    viloyati = models.TextField()
    fakulteti = models.CharField(max_length=40)
    kursi = models.IntegerField(default=1)
    guruhi = models.CharField(max_length=20)

class Ins1(models.Model):
    respublikasi = models.CharField(max_length=20)
    viloyati = models.CharField(max_length=20)
    fakultetlarisoni = models.IntegerField(default=2)
    yonalishi = models.CharField(max_length=20)

class Ins2(models.Model):
    kursi = models.IntegerField(default=1)
    guruhi = models.CharField(max_length=10)
    talabalarisoni = models.IntegerField(default=500)
    talabasi=models.TextField()

    
