# Generated by Django 4.1.7 on 2023-02-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libreria', '0008_autor_apodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='apellido',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='apodo',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]