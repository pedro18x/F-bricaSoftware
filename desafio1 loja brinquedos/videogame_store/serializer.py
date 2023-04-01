from rest_framework import serializers
from .models import Brinquedo, Loja, Cliente

class BrinquedoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brinquedo
        fields = ['nome', 'preco']

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'telefone']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone']                
