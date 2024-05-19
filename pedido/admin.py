from django.contrib import admin
from .models import Pedido, PedidoPrato

class PedidoPratoInline(admin.TabularInline):
    model = PedidoPrato
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_pedido', 'status', 'valor_total', 'desconto')
    list_filter = ('status', 'data_pedido')
    search_fields = ('cliente__nome_completo', 'cliente__cpf')
    ordering = ('-data_pedido',)
    inlines = [PedidoPratoInline]