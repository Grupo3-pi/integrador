from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'email', 'celular', 'data_cadastro')
    search_fields = ('nome_completo', 'cpf', 'email')
    list_filter = ('data_cadastro',)
    ordering = ('-data_cadastro',)