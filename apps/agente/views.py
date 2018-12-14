# from django.shortcuts import render
from apps.agente.models import Agente
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


def get_Agente(request):
    agente = {}
    numero = request.GET.get('numero')
    try:
        queryset = Agente.objects.get(NroDocumento=numero)
        agente = {
            'nombre': "%s %s" % (queryset.Apellido, queryset.Nombre)
        }
    except ObjectDoesNotExist:
        agente = {
            'NoMatch': 'Agente no registrado...',
        }
    return JsonResponse(agente)
