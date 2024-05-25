from django.db import models
from cliente.models import Cliente
from cardapio.models import Prato
from django.contrib.auth.models import User

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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nome_completo}'

    def calcular_valor_total(self):
        total = 0
        pedido_pratos = PedidoPrato.objects.filter(pedido=self)
        for pedido_prato in pedido_pratos:
            total += (pedido_prato.preco_unitario - pedido_prato.desconto_unitario) * pedido_prato.quantidade
        self.valor_total = total
        self.save()

class PedidoPrato(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    desconto_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not self.preco_unitario:
            self.preco_unitario = self.prato.valor
        super().save(*args, **kwargs)
        self.pedido.calcular_valor_total()

    def __str__(self):
        return f'{self.quantidade} x {self.prato.nome_prato} no pedido {self.pedido.id}'