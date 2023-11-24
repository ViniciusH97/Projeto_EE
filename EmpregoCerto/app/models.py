from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    telefone = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=50)
    segmento = models.CharField(max_length=100)
    
    def __str__(self):
        return self.razao_social
    
class Vaga(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class Candidato(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=40)
    email = models.EmailField(max_length=30, unique=True)

    def __str__(self):
        return self.nome