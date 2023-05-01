from django.db import models

class Ingredientes(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome

class Prato(models.Model):
    nome_prato = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome_prato

class Cardapio(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.DO_NOTHING)
    Ingrediente = models.ForeignKey(Ingredientes, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.prato
