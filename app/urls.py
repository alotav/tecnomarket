from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import home, contacto, galeria, agregar_producto, listar_productos, editar_productos, eliminar_productos, registro, ProductoViewset, error_facebook


# rest framework
router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('editar-productos/<id>/', editar_productos, name='editar_productos'),
    path('eliminar-productos/<id>/', eliminar_productos, name='eliminar_productos'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name='error_facebook')
]