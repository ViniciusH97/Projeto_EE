from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    pessoa_fisica = models.BooleanField(default=True)
    pessoa_juridica = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

class Empresa(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    razao_social = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=50)
    segmento = models.CharField(max_length=255)
    
class Vaga(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

class Candidato(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=40)
    email = models.EmailField(max_length = 30, unique=True)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Nome de usuário')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    
