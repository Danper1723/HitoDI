from django.db import models

class Tienda(models.Model):
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20)
    imagen = models.FilePathField(path="/img")