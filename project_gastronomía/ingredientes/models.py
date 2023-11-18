from django.db import models
from productos.models import Producto
from categoria.models import Categoria

class Ingredientes(models.Model):
    nombreIngrediente = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto,  on_delete=models.CASCADE, related_name='ingredientes', default=1)  
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='ingredientes', default=1)
   

    def __str__(self):
        return self.nombreIngrediente
