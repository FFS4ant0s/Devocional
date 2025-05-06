# users/models.py
# flake8: noqa: E501
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    usuario = models.CharField(max_length=50)
    pass


class Tema(models.Model):
    nome = models.CharField(max_length=255)

    # E-mail, já incluído no AbstractUser, mas pode ser personalizado
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"


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
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='logenvios_users')
    data_envio = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Log de envio para {self.usuario.nome} ({self.usuario.email}) em {self.data_envio}"
