from django.db import models

# Create your models here.
class Colores(models.Model):
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.color} {self.marca}'
