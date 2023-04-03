from django.contrib import admin
from .models import Paciente, Enfermeiro

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'id_paciente')
    
admin.site.register(Paciente, PacienteAdmin)


class EnfermeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'id_funcionario')

admin.site.register(Enfermeiro, EnfermeiroAdmin)