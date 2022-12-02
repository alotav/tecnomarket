from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ['nombre', 'contacto', 'tipo_consulta', 'mensaje', 'avisos']
        
        # Con  __all__ toma todos los campos del model sin tener que declararlos como en la linea anterior.
        fields = '__all__'