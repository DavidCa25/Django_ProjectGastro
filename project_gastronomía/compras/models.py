from django.db import models
from ingredientes.models import Ingredientes
from usuarios.models import Usuario

class Compra(models.Model):
    Id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    nombre = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, related_name="compra_nombre", default=1)
    precio = models.ForeignKey(Ingredientes, on_delete=models.CASCADE, related_name='compra_precio', default=1)
   