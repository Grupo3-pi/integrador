from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from pedido.models import Pedido, PedidoPrato
from cardapio.models import Cardapio
from datetime import date

def calcular_idade(data_nascimento):
    today = date.today()
    return today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))

def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def flexmonster_view(request):
    data_url = request.build_absolute_uri('/analise/flexmonster_data/')
    return render(request, 'analise/flexmonster.html', {'data_url': data_url})

@login_required
@user_passes_test(superuser_required)
def flexmonster_data(request):
    pedidos = Pedido.objects.all().select_related('cliente').prefetch_related('pedidoprato_set__prato')

    data = []

    for pedido in pedidos:
        for item in pedido.pedidoprato_set.all():
            prato = item.prato
            ingredientes = Cardapio.objects.filter(prato=prato).select_related('Ingrediente')

            for ing in ingredientes:
                ingrediente_nome = ing.Ingrediente.nome

                data.append({
                    "id_pedido": pedido.id,
                    "cliente_nome": pedido.cliente.nome_completo,
                    "cliente_bairro": pedido.cliente.bairro,
                    "cliente_cpf": pedido.cliente.cpf,
                    "cliente_cidade": pedido.cliente.cidade,
                    "prato": prato.nome_prato,
                    "ingrediente": ingrediente_nome,  # Cada ingrediente adicionado individualmente
                    "quantidade": item.quantidade,
                    "data_pedido": pedido.data_pedido,
                    "valor_total": pedido.valor_total,
                    "vendedor": pedido.usuario.get_username() if pedido.usuario else None,
                    "cliente_idade": calcular_idade(pedido.cliente.data_nascimento) if pedido.cliente.data_nascimento else None,
                })

    return JsonResponse(data, safe=False)