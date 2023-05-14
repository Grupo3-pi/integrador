from django.shortcuts import render
from .models import Cardapio

def cardapio(request):
    cardapio_list = Cardapio.objects.all()
    return render(request, 'cardapio.html', {'Cardapio': cardapio_list})