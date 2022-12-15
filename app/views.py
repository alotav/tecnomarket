from django.shortcuts import render, redirect, render, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.


def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)



def contacto(request):
    data = {
       'form': ContactoForm(),
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = '*Mensaje enviado'
        else:
            data['form'] = formulario
    
    return render(request, 'app/contacto.html', data)



def galeria(request):
    return render(request, 'app/galeria.html')



def agregar_producto(request):

    data = {
        'form':ProductoForm(),
    }

    if request.method == 'POST':
        # Guardamos en la variable formulario los datos que se envian desde el form.
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
            data['mensaje'] = '*Datos guardados correctamente.'
        else:
            data['form'] = formulario

    return render (request, 'app/producto/agregar.html', data)


def listar_productos(request):
    productos = Producto.objects.all()
    # obtenemos el valor de page a traves de la url, en caso contrario el valor sera 1
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }


    return render(request, 'app/producto/listar.html', data)

    
    
def editar_productos(request, id):
    # Producto.objects.get(id=id)
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to='listar_productos')
        data['form']=formulario

    return render(request, 'app/producto/modificar.html', data)


def eliminar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request,'El producto fue eliminado.')
    return redirect(to='listar_productos')