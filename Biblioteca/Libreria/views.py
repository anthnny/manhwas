from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def contacto(request):
    return render(request, 'paginas/contacto.html')

def autores(request):
    query = request.GET.get('q')
    if query:
        autores = Autor.objects.filter(
            Q(id__icontains=query) | Q(nombre__icontains=query) | Q(apodo__icontains=query)
        )
    else:
        autores = Autor.objects.all().order_by('id')
    return render(request, 'autores/autores.html', {'autores': autores})

def autor_crear(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorForm()
    return render(request, 'autores/crear.html', {'formulario': form})

def autor_editar(request,id):
    autor = get_object_or_404(Autor, pk=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autores/editar.html', {'formulario': form})

def autor_eliminar(request, id):
    try:
        autor = get_object_or_404(Autor, id=id)
        libros = Libro.objects.filter(autor=autor)
        libros.delete()
        autor.delete()
        return JsonResponse({'mensaje': 'Autor eliminado correctamente.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)







def libros(request):
    query = request.GET.get('q')
    if query:
        libros = Libro.objects.filter(
            Q(id__icontains=query) | Q(titulo__icontains=query)
        )
    else:
        libros = Libro.objects.all()
    return render(request, 'libros/libros.html', {'libros': libros})

def libro_crear(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear.html', {'formulario': form})

def libro_editar(request,id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar.html', {'formulario': form})



def libro_eliminar(request, id):
    try:
        libro = get_object_or_404(Libro, id=id)
        autor = libro.autor
        libro.delete()
        autor.save()
        return JsonResponse({'mensaje': 'Libro eliminado correctamente.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)