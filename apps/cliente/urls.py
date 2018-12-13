from django.urls import path
from apps.cliente.views import Registrar_Cliente, get_Cliente

urlpatterns = [
    path('registrar/', Registrar_Cliente, name='registrar_cliente'),
    path('ajax/get_cliente/', get_Cliente, name='ajax_get_cliente'),
]
