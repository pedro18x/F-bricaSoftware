from rest_framework import viewsets
from .models import Brinquedo, Loja, Cliente
from .serializer import BrinquedoSerializer, LojaSerializer, ClienteSerializer


class BrinquedoViewSet(viewsets.ModelViewSet):
    queryset = Brinquedo.objects.all()
    serializer_class = BrinquedoSerializer    

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
