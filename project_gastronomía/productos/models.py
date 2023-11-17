from django.db import models
from categoria.models import Categoria

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombreProducto
