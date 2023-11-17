from django.db import models

class Vendedor(models.Model):
    nombreVendedor = models.CharField(max_length=255)
    tipo_vendedor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreVendedor
