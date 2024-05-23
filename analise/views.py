from django.shortcuts import render
from django.http import JsonResponse
from pedido.models import Pedido, PedidoPrato
from datetime import date

def calcular_idade(data_nascimento):
    today = date.today()
    return today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))

def flexmonster_view(request):
    data_url = request.build_absolute_uri('/analise/flexmonster_data/')
    return render(request, 'analise/flexmonster.html', {'data_url': data_url})

def flexmonster_data(request):
    pedidos = Pedido.objects.all().select_related('cliente').prefetch_related('pedidoprato_set__prato')
    data = [
        {
            "id_pedido": pedido.id,
            "cliente_nome": pedido.cliente.nome_completo,
            "cliente_cpf": pedido.cliente.cpf,
            "cliente_cidade": pedido.cliente.cidade,
            "prato": item.prato.nome_prato,
            "quantidade": item.quantidade,
            "data_pedido": pedido.data_pedido,
            "cliente_idade": calcular_idade(pedido.cliente.data_nascimento) if pedido.cliente.data_nascimento else None,
        }
        for pedido in pedidos
        for item in pedido.pedidoprato_set.all()
    ]
    return JsonResponse(data, safe=False)