# Creamos validadores personalizados
from django.forms import ValidationError
# Validador para tamaño maximo de archivo adjunto:

class MaxSizeFileValidator:

    def __init__(self, max_size_file= 5):
        self.max_size_file = max_size_file

    def __call__(self, value):
        size = value.size
        max_size = self.max_size_file * 1048576

        if size > max_size:
            raise ValidationError(f'El tamaño maximo del archivo debe ser de {self.max_size_file}MB.')
        
        return value