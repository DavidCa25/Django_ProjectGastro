from django.db import models

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombreCategoria

