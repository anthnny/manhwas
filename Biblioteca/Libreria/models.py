from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=True,null=True, default='')
    apellido = models.CharField(max_length=200, blank=True,null=True, default='')
    apodo = models.CharField(max_length=100, blank=True, null=True, default='')
    nacionalidad =models.CharField(max_length=100, blank=False,null=False)
    correo = models.EmailField(blank=False, null=False, default='') 
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True,auto_now_add=False)
    
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
        
    def __str__(self):
        if self.apodo:
            return self.apodo
        else:
            return f"{self.nombre} {self.apellido}"
    


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    descripcion = models.TextField('Descripcion', max_length=1300, blank=False, null=False, default='')
    fecha_publicacion = models.DateField('Fecha de publicacion', blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
        
    def __str__(self):
        return f"{self.titulo} - {self.autor} (ID: {self.autor.id})"
    
    
    
class ObraLiteraria(models.Model):
    titulo = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField('Descripcion', max_length=1300, blank=False, null=False, default='')
    autores = models.ManyToManyField(Autor)
    fecha_publicacion = models.DateField()
    
    class Meta:
        verbose_name = 'Obra Literaria'
        verbose_name_plural = 'Obras Literarias'
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo