from django.shortcuts import render, redirect
from .models import Cliente, Pedido, Prato, PedidoPrato
from django.http import JsonResponse
from cliente.models import Cliente
from cardapio.models import Prato
from django.contrib.auth.decorators import login_required  # Importe o decorador de autenticação

def checkout(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        cliente = Cliente.objects.filter(cpf=cpf).first()
        pratos = Prato.objects.all()
        return render(request, 'pedido/checkout.html', {'cliente': cliente, 'pratos': pratos})
    return render(request, 'pedido/checkout.html', {'pratos': Prato.objects.all()})

@login_required  # Adicione o decorador de autenticação para garantir que o usuário esteja autenticado
def processar_pedido(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        pratos_selecionados = [int(key.replace('prato', '')) for key in request.POST.keys() if key.startswith('prato') and key.replace('prato', '').isdigit()]
        pratos = Prato.objects.filter(id__in=pratos_selecionados)
        
        # Obter o usuário autenticado
        usuario = request.user

        # Verifica se o cliente existe
        cliente = Cliente.objects.filter(cpf=cpf).first()
        if cliente:
            # Cria um novo pedido com o usuário autenticado
            pedido = Pedido.objects.create(cliente=cliente, usuario=usuario)
            # Adiciona os pratos ao pedido
            for prato in pratos:
                quantidade = request.POST.get(f'prato{prato.id}', 0)
                PedidoPrato.objects.create(pedido=pedido, prato=prato, quantidade=quantidade)
            
            # Redireciona para alguma página de confirmação ou agradecimento
            return redirect('pagina_de_confirmacao')
        else:
            # Redireciona de volta à página de checkout com uma mensagem de erro
            return render(request, 'checkout.html', {'error_message': 'Cliente não encontrado.'})
    else:
        return redirect('checkout')

def obter_cliente_id(request):
    if request.method == 'GET':
        cpf = request.GET.get('cpf')
        if cpf:  # Verifica se o CPF não está vazio
            cliente = Cliente.objects.filter(cpf=cpf).first()
            if cliente:
                return JsonResponse({'cliente_id': cliente.cpf, 'cliente_nome': cliente.nome_completo})
            else:
                return JsonResponse({'error': 'Cliente não encontrado.'})
        else:
            return JsonResponse({'error': 'CPF não fornecido.'})
            