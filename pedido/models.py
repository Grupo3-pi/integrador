from django.db import models
from django.db import models
from cliente.models import Cliente
from cardapio.models import Prato

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('E', 'Em Preparo'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pratos = models.ManyToManyField(Prato, through='PedidoPrato')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_valor_total(self):
        total = sum(item.quantidade * item.prato.valor for item in self.pedidoprato_set.all())
        total_com_desconto = total - self.desconto
        self.valor_total = max(total_com_desconto, 0)  # Garante que o valor total não seja negativo
        self.save()

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nome_completo}'

class PedidoPrato(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade} x {self.prato.nome_prato} no pedido {self.pedido.id}'