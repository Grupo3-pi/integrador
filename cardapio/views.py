from django.shortcuts import render
from .models import Cardapio, Prato, Ingredientes


def cardapio(request):
    prato_list = Prato.objects.all().order_by('nome_prato')
    ingrediente_list = Ingredientes.objects.all().order_by('nome')
    return render(request, 'cardapio.html', {'prato': prato_list, 'Ingredientes': ingrediente_list})
