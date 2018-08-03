from django.db import models

# Create your models here.

class Opcion(models.Model):
    opcion = models.CharField(max_length=200)
    def __str__(self):
        return self.opcion


class Letra(models.Model):
    letra = models.CharField(max_length=200)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    def __str__(self):
        return self.letra
    