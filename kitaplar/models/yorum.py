from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from kitaplar.models import Kitap

class Yorum(models.Model):
    kitap = models.ForeignKey(Kitap, on_delete=models.CASCADE, related_name='yorumlar')

    yorum_sahibi = models.CharField(max_length=50)
    yorum = models.TextField(blank=True, null=True)

    yaratilma_tarihi = models.DateTimeField(auto_now_add=False)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    degerlendirme = models.PositiveIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return self.yorum_sahibi


