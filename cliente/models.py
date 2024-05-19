from django.db import models

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)  
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True) 
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome_completo} - {self.cpf}'