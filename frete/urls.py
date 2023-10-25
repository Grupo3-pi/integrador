from django.urls import path
from .views import calcula_frete

urlpatterns = [
    path('calcula_frete/', calcula_frete, name='calcula_frete'),
]