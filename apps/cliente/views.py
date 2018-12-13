from django.shortcuts import render
from apps.cliente.forms import Registrar_Cliente_Form
from apps.cliente.models import Cliente
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def Registrar_Cliente(request):
    template_name = 'cliente/registrar_cliente.html'
    form = Registrar_Cliente_Form()
    successful_data = False
    if request.method == "POST":
        form = Registrar_Cliente_Form(request.POST)
        if form.is_valid():
            obj = Cliente()
            obj.Usuario = request.user
            obj.SectorEconomico = form.cleaned_data.get("SectorEconomico")
            obj.TipoPersona = form.cleaned_data.get("TipoPersona")
            obj.PaisDoc = form.cleaned_data.get("PaisDocumento")
            obj.TipoDocumento = form.cleaned_data.get("TipoDoc")
            obj.NumeroDocumento = form.cleaned_data.get("NroDoc")
            obj.Apellido = form.cleaned_data.get("PrimerApellido")
            obj.Nombre = form.cleaned_data.get("PrimerNombre")
            obj.NombreCompleto = form.cleaned_data.get("NombreCompleto")
            obj.FechaNacimiento = form.cleaned_data.get("FechaNacimiento")
            obj.Genero = form.cleaned_data.get("Genero")
            obj.EstadoCivil = form.cleaned_data.get("EstadoCivil")
            obj.Nacionalidad = form.cleaned_data.get("Nacionalidad")
            obj.Telefono = form.cleaned_data.get("Telefono")
            obj.TipoDireccion = form.cleaned_data.get("TipoDireccion")
            obj.Pais = form.cleaned_data.get("Pais")
            obj.Departamento = form.cleaned_data.get("Departamento")
            obj.Ciudad = form.cleaned_data.get("Ciudad")
            obj.Barrio = form.cleaned_data.get("Barrio")
            obj.DireccionLibre = form.cleaned_data.get("DireccionLibre")
            obj.ComprobanteIngreso = form.cleaned_data.get(
                "ComprobanteIngreso"
            )
            obj.Salario = form.cleaned_data.get("Salario")
            obj.CargoTrabajo = form.cleaned_data.get("CargoTrabajo")
            obj.Dependiente = form.cleaned_data.get("EsDependiente")
            obj.save()
            print(obj.idCliente)
            successful_data = True
            form = Registrar_Cliente_Form()
            return render(
                request,
                template_name,
                {
                    'form': form,
                    'successful_data': successful_data,
                    'NroCliente': obj.idCliente,
                }
            )
        else:
            print(form.errors)
    return render(
        request,
        template_name,
        {
            'form': form,
            'successful_data': successful_data,
        }
    )


def get_Cliente(request):
    cliente = {}
    numero = request.GET.get('numero')
    try:
        queryset = Cliente.objects.get(NumeroDocumento=numero)
        cliente = {
            'nombre': queryset.NombreCompleto,
            'sector': queryset.get_SectorEconomico_display(),
            'telefono': queryset.Telefono,
            'direccion': queryset.DireccionLibre,
        }
    except ObjectDoesNotExist:
        cliente = {
            'NoMatch': 'Cliente no registrado...',
        }
    return JsonResponse(cliente)
