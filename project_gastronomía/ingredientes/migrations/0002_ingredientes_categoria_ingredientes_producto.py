# Generated by Django 4.2.5 on 2023-11-16 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('productos', '0001_initial'),
        ('ingredientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientes',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='categoria.categoria'),
        ),
        migrations.AddField(
            model_name='ingredientes',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='productos.producto'),
        ),
    ]
