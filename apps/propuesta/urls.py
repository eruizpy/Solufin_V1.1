from django.urls import path
from apps.propuesta.views import Registrar_Propuesta

urlpatterns = [
    path('registrar/', Registrar_Propuesta, name='registrar_propuesta'),
]
