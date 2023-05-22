from django.shortcuts import render
from .models import Cardapio, Prato, Ingredientes


def cardapio(request):
    prato_list = Prato.objects.all()
    return render(request, 'cardapio.html', {'prato': prato_list})
