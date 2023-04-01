from django.contrib import admin
from .models import Brinquedo, Loja, Cliente

class BrinquedoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(Brinquedo, BrinquedoAdmin)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Loja, LojaAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Cliente, ClienteAdmin)    

