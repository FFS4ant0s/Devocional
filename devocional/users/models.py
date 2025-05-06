# Importa o modelo base de usuário do Django
from django.contrib.auth.models import AbstractUser
# Importa o módulo de models
from django.db import models

# Define o modelo de usuário customizado herdando de AbstractUser


class User(AbstractUser):
    # Substitui o campo de e-mail para ser único no sistema
    email = models.EmailField(unique=True)

    # Retorna o nome de usuário como representação do objeto
    def __str__(self):
        return self.username
