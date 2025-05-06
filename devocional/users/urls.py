# users/urls.py
# flake8: noqa: E501
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TemaViewSet, DevocionalViewSet, VersiculoViewSet, LogEnvioViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'temas', TemaViewSet)
router.register(r'devocionais', DevocionalViewSet)
router.register(r'versiculos', VersiculoViewSet)
router.register(r'logenvios', LogEnvioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
