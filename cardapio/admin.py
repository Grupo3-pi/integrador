from django.contrib import admin
from .models import Cardapio, Prato, Ingredientes

admin.site.site_header = "Painel Administrativo"
admin.site.index_title = "Hangar 252"
admin.site.site_title = "Painel Administrativo"


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display=('id','prato','Ingrediente')
    list_display_links=('id','prato','Ingrediente')
    list_filter=('prato','Ingrediente')

@admin.register(Ingredientes)
class IngredientesAdmin(admin.ModelAdmin):
    list_display=('id','nome','tipo')
    list_display_links=('id','nome')
    list_filter=('tipo',)
    search_fields=('nome',)

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display=('id','nome_prato','tipo','descricao','foto')
    list_display_links=('id','nome_prato')
    list_editable=('nome_prato','foto')
    list_filter=('tipo',)
    search_fields=('nome_prato',)
