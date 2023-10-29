from django.contrib import admin
from .models import Hamburgueria, FaixaFrete

admin.site.site_header = "Painel Administrativo"
admin.site.index_title = "Hangar 252"
admin.site.site_title = "Painel Administrativo"


@admin.register(Hamburgueria)
class HamburgueriaAdmin(admin.ModelAdmin):
    list_display=('nome','latitude','longitude')


@admin.register(FaixaFrete)
class FaixaFreteAdmin(admin.ModelAdmin):
    list_display=('hamburgueria','distancia_minima','distancia_maxima','valor_frete')
