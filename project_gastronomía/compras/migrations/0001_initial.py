# Generated by Django 4.2.5 on 2023-11-16 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('Id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
