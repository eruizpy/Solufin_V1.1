from django.shortcuts import render
from apps.propuesta.forms import Propuesta_Form


def Registrar_Propuesta(request):
    Template_Name = "propuesta/propuesta.html"
    return render(
        request,
        Template_Name,
        {
            'propuesta': Propuesta_Form,
        },
    )
