from django.contrib import admin
from .models import Cardapio, Prato, Ingredientes

admin.site.register(Cardapio)
admin.site.register(Prato)
admin.site.register(Ingredientes)