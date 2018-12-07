from django.shortcuts import render
from apps.cliente.forms import Registrar_Cliente_Form
from apps.cliente.models import Cliente as Clientes


def Registrar_Cliente(request):
    template_name = 'cliente/registrar_cliente.html'
    form = Registrar_Cliente_Form()
    if request.method == "POST":
        obj = Clientes()
        form = Registrar_Cliente_Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(obj)
        else:
            print(form.errors)
    return render(
        request,
        template_name,
        {
            'form': form,
        }
    )
