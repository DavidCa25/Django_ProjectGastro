# Generated by Django 4.2.5 on 2023-11-16 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_compra_nombre_compra_precio'),
        ('historialCompras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialcompras',
            name='IdCompra',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='compras.compra'),
        ),
    ]
