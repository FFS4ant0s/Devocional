# users/serializers.py
# flake8: noqa: E501
from rest_framework import serializers
from .models import User, Tema, Devocional, Versiculo, LogEnvio


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'


class DevocionalSerializer(serializers.ModelSerializer):
    tema = TemaSerializer()  # Embedding Tema data into Devocional

    class Meta:
        model = Devocional
        fields = '__all__'


class VersiculoSerializer(serializers.ModelSerializer):
    devocional = DevocionalSerializer()  # Embedding Devocional data into Versiculo

    class Meta:
        model = Versiculo
        fields = '__all__'


class LogEnvioSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()  # Embedding User data into LogEnvio

    class Meta:
        model = LogEnvio
        fields = '__all__'
