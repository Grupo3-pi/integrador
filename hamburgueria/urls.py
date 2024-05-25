from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cardapio.urls')),
    path('', include('frete.urls')),
    path('analise/', include('analise.urls')),
    path('pedido/', include('pedido.urls')),
    path('', include('login.urls')), 
]