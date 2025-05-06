# Importa o módulo de models do Django
from django.db import models
# Importa o modelo de usuário configurado no projeto
from django.conf import settings

# Modelo para cadastrar os temas dos devocionais
# flake8: noqa: E501


class Tema(models.Model):
    # Nome do tema (Ex: Fé, Gratidão, Coragem)
    nome = models.CharField(max_length=100)
    # Descrição opcional para detalhar o tema
    descricao = models.TextField(blank=True, null=True)

    # Retorna o nome como representação do objeto
    def __str__(self):
        return self.nome


# Modelo para os devocionais
class Devocional(models.Model):
    # Título do devocional (Ex: Confiança em Deus)
    titulo = models.CharField(max_length=200)
    # Mensagem ou texto principal do devocional
    mensagem = models.TextField()
    # Relaciona o devocional a um tema
    tema = models.ForeignKey(
        Tema,                       # Modelo relacionado
        on_delete=models.CASCADE,   # Se o tema for deletado, deleta os devocionais ligados
        related_name='devocionais'  # Nome para acessar os devocionais a partir do tema
    )
    # Data e hora de criação automática
    criado_em = models.DateTimeField(auto_now_add=True)

    # Retorna o título como representação do objeto
    def __str__(self):
        return self.titulo


# Modelo para os versículos bíblicos
class Versiculo(models.Model):
    # Texto completo do versículo
    texto = models.TextField()
    # Referência bíblica (Ex: João 3:16)
    referencia = models.CharField(max_length=100)
    # Relaciona o versículo a um devocional
    devocional = models.ForeignKey(
        Devocional,                     # Modelo relacionado
        on_delete=models.CASCADE,       # Se o devocional for deletado, deleta os versículos
        # Nome para acessar os versículos a partir do devocional
        related_name='versiculos'
    )

    # Retorna a referência + um pedaço do texto como representação do objeto
    def __str__(self):
        return f"{self.referencia} - {self.texto[:30]}..."


# Modelo para registro de envios de devocionais
class LogEnvio(models.Model):
    # Usuário para quem o devocional foi enviado
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,       # Usa o modelo de usuário configurado
        on_delete=models.CASCADE,       # Se o usuário for deletado, deleta os logs
        related_name='logenvios_core'
    )
    # Devocional enviado
    devocional = models.ForeignKey(
        Devocional,                     # Modelo relacionado
        on_delete=models.CASCADE        # Se o devocional for deletado, deleta os logs
    )
    # Data e hora em que foi enviado (adicionada automaticamente)
    enviado_em = models.DateTimeField(auto_now_add=True)
    # Status do envio (Ex: enviado, erro, pendente)
    status = models.CharField(max_length=50)
    # Mensagem de retorno ou erro, caso haja
    mensagem_retorno = models.TextField(blank=True, null=True)

    # Retorna uma string resumida do envio
    def __str__(self):
        return f"Envio de {self.devocional.titulo} para {self.user.username} em {self.enviado_em}"
