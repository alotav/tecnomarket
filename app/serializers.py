from rest_framework import serializers
from .models import Producto, Marca


# Agregar serializador para marca:
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marca
        fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    # Agregar campo al JSON:
    # nombre_marca = serializers.CharField(read_only=True, source='marca.nombre')
    # Agregar serializador relacionado para marca:
    marca = MarcaSerializer(read_only=True)
    # Agregamos validacion:
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source='marca')
    nombre = serializers.CharField(required=True, min_length=3)
    
    # Validacion personalizada:
    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()
        
        if existe:
            raise serializers.ValidationError("Este nombre ya existe")
        
        else:
            return value

    class Meta:
        model = Producto
        fields = '__all__'