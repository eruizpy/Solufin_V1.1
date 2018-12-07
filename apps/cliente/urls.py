from django.urls import path
from apps.cliente.views import Registrar_Cliente

urlpatterns = [
    path('registrar/', Registrar_Cliente, name='registrar_cliente'),
]
