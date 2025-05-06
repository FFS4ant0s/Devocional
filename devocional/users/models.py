# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Aqui você pode adicionar campos personalizados, se necessário
    pass


class Tema(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Devocional(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f"Devocional sobre {self.tema.nome}"


class Versiculo(models.Model):
    devocional = models.ForeignKey(Devocional, on_delete=models.CASCADE)
    versiculo = models.CharField(max_length=255)

    def __str__(self):
        return self.versiculo


class LogEnvio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_envio = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Log de envio para {self.usuario} em {self.data_envio}"
