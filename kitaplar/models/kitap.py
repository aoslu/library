from django.db import models
#from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here

class Kitap(models.Model):
    isim = models.CharField(max_length=50)
    yazar = models.CharField(max_length=50)
    aciklama = models.TextField()

    yaratilma_tarihi = models.DateTimeField(auto_now_add=False)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    yayin_tarihi = models.DateTimeField()

    def __str__(self):
        return f'{self.isim} - {self.yazar}'



