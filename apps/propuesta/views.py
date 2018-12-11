from django.shortcuts import render


def Registrar_Propuesta(request):
    Template_Name = "propuesta/propuesta.html"
    return render(
        request,
        Template_Name,
    )
