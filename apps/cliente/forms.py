from django import forms
from apps.cliente.choices import *
from apps.cliente.models import Cliente as ClienteModel
import datetime


class Registrar_Cliente_Form(forms.Form):
    SectorEconomico = forms.ChoiceField(
        label='Sector Economico',
        choices=SectoresEconomicos,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    PaisDocumento = forms.ChoiceField(
        label='Tipo de Persona',
        choices=PaisDoc,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    TipoPersona = forms.ChoiceField(
        label='Tipo de Persona',
        choices=TipoPersona,
        initial=1,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    NroDoc = forms.CharField(
        label='Numero de Documento',
        max_length=10,
        strip=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    TipoDoc = forms.ChoiceField(
        label='Tipo de Documento',
        initial=4,
        choices=TipoDoc,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    PrimerApellido = forms.CharField(
        label='Apellido/s',
        max_length=30,
        strip=True,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    PrimerNombre = forms.CharField(
        label='Nombre',
        max_length=30,
        strip=True,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    NombreCompleto = forms.CharField(
        label='Nombre Completo',
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    FechaNacimiento = forms.CharField(
        label='Fecha de Nacimiento',
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'dd/mm/yyyy',
            },
        ),
    )
    Nacionalidad = forms.ChoiceField(
        label='Nacionalidad',
        choices=Nacionalidad,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    EstadoCivil = forms.ChoiceField(
        label='Estado Civil',
        choices=EstadoCivil,
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Genero = forms.ChoiceField(
        label='Genero',
        initial='M',
        choices=Generos,
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Telefono = forms.CharField(
        label='Telefono',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    TipoDireccion = forms.ChoiceField(
        label='Tipo de Direccion',
        choices=TipoDireccion,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Pais = forms.ChoiceField(
        label='Pais',
        choices=Pais,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Departamento = forms.ChoiceField(
        label='Departamento',
        choices=Departamentos,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Ciudad = forms.CharField(
        label='Ciudad',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Barrio = forms.CharField(
        label='Ciudad',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    DireccionLibre = forms.CharField(
        label='Direccion Libre',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    ComprobanteIngreso = forms.CharField(
        label='Comprobante de Ingreso',
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    Salario = forms.CharField(
        label='Salario',
        max_length=9,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    CargoTrabajo = forms.CharField(
        label='Cargo en el trabajo',
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    EsDependiente = forms.ChoiceField(
        label='Comprobante de Ingreso',
        choices=EsDependiente,
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    def clean_FechaNacimiento(self, *args, **kwargs):
        Nacimiento = self.cleaned_data.get("FechaNacimiento")
        if Nacimiento == '':
            return None
        else:
            fecha = datetime.datetime.strptime(
                Nacimiento,
                "%d/%m/%Y",
            ).strftime("%Y-%m-%d")
            return fecha

    def clean_NroDoc(self, *args, **kwargs):
        documento = self.cleaned_data.get("NroDoc")
        try:
            queryset = ClienteModel.objects.get(NumeroDocumento=documento)
            if queryset:
                raise forms.ValidationError(
                    "Usuario %s ya esta registrado" % queryset
                )
        except ClienteModel.DoesNotExist:
            return documento
