from django.contrib import admin
from .models import Producto, Marca, Contacto
from .forms import ProductoForm
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'nuevo', 'marca']
    list_editable = ['precio']
    search_fields = ['nombre']
    list_filter = ['marca', 'nuevo']
    list_per_page: 5
    # Usar form personalizado con validaciones:
    form = ProductoForm

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca)
admin.site.register(Contacto)