from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PacienteSerializer, EnfermeiroSerializer
from .models import Paciente, Enfermeiro


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class EnfermeiroViewSet(viewsets.ModelViewSet):
    queryset = Enfermeiro.objects.all()
    serializer_class = EnfermeiroSerializer