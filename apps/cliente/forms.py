from django import forms
from apps.cliente.choices import (
    SectoresEconomicos,
    TipoDoc,
    TipoPersona,
    Nacionalidad,
    EstadoCivil,
    Generos,
    TipoDireccion,
    Pais,
    Departamento
)


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
    IdTipoDoc = forms.ChoiceField(
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
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
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
        choices=Departamento,
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
