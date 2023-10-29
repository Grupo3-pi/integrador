from django.db import models

from django.db import models

class Hamburgueria(models.Model):
    nome = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=18, decimal_places=14)
    longitude = models.DecimalField(max_digits=18, decimal_places=14)

    def __str__(self):
        return self.nome
    
class FaixaFrete(models.Model):
    hamburgueria = models.ForeignKey(Hamburgueria, on_delete=models.CASCADE)
    distancia_minima = models.DecimalField(max_digits=10, decimal_places=2)
    distancia_maxima = models.DecimalField(max_digits=10, decimal_places=2)
    valor_frete = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Faixa de {self.distancia_minima} a {self.distancia_maxima} km: R${self.valor_frete}'