from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Usamos el validador para tamaño de adjunto
from .validators import MaxSizeFileValidator
from django.forms import ValidationError


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ['nombre', 'contacto', 'tipo_consulta', 'mensaje', 'avisos']
        
        # Con  __all__ toma todos los campos del model sin tener que declararlos como en la linea anterior.
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    # Modificamos la validacion del form:
    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_size_file=2)])
    precio = forms.IntegerField(min_value=1, max_value=1000000)

    # Validamos que el producto no se repita:
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe.")

        return nombre

    class Meta:
        model = Producto
        fields = '__all__'

        # Para que podamos elegir la fecha en el html, agregamos un widget:
        widgets = {
            'fecha_fabricacion': forms.SelectDateWidget() 
        }


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
    