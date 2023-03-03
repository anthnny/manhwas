from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('autores', views.autores, name='autores'),
    path('autores/crear', views.autor_crear, name='autor_crear'),
    path('autores/editar', views.autor_editar, name='autor_editar'),
    path('autores/editar/<int:id>', views.autor_editar, name='autor_editar'),
    path('autores/eliminar/<int:id>', views.autor_eliminar, name='autor_eliminar'),
    
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.libro_crear, name='libro_crear'),
    path('libros/editar', views.libro_editar, name='libro_editar'),
    path('libros/editar/<int:id>', views.libro_editar, name='libro_editar'),
    path('libros/eliminar/<int:id>', views.libro_eliminar, name='libro_eliminar'),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)