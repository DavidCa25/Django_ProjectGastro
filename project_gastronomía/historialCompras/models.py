from django.db import models
from compras.models import Compra

class HistorialCompras(models.Model):
    IdCompra = models.ForeignKey(Compra, on_delete=models.CASCADE, default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra #{self.IdCompra} - Total: {self.total}"