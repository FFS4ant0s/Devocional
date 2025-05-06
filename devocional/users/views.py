# users/views.py
# flake8: noqa: E501
from rest_framework import viewsets
from .models import User, Tema, Devocional, Versiculo, LogEnvio
from .serializers import UserSerializer, TemaSerializer, DevocionalSerializer, VersiculoSerializer, LogEnvioSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer


class DevocionalViewSet(viewsets.ModelViewSet):
    queryset = Devocional.objects.all()
    serializer_class = DevocionalSerializer


class VersiculoViewSet(viewsets.ModelViewSet):
    queryset = Versiculo.objects.all()
    serializer_class = VersiculoSerializer


class LogEnvioViewSet(viewsets.ModelViewSet):
    queryset = LogEnvio.objects.all()
    serializer_class = LogEnvioSerializer
