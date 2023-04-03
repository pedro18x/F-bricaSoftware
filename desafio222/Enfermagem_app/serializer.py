from rest_framework import serializers
from .models import Paciente, Enfermeiro

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'id_paciente']

class EnfermeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiro
        fields = ['nome', 'turno', 'id_funcionario']


