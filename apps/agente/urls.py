from django.urls import path
from apps.agente.views import get_Agente


urlpatterns = [
    path('ajax/get_agente/', get_Agente, name='ajax_get_agente'),
]
