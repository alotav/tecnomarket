from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ['nombre', 'contacto', 'tipo_consulta', 'mensaje', 'avisos']
        
        # Con  __all__ toma todos los campos del model sin tener que declararlos como en la linea anterior.
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    

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
    