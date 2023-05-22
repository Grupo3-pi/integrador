from django.contrib import admin
from .models import Cardapio, Prato, Ingredientes

@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display=('id','prato','Ingrediente')
    list_filter=('prato','Ingrediente')

@admin.register(Ingredientes)
class IngredientesAdmin(admin.ModelAdmin):
    list_display=('id','nome','tipo')
    list_filter=('tipo',)
    search_fields=('nome',)

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display=('id','nome_prato','tipo','descricao','foto')
    list_display_links=('id','nome_prato')
    list_filter=('tipo',)
    search_fields=('nome_prato',)
