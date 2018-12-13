from django import forms
from django.forms import formset_factory
from apps.propuesta.choices import *


class Propuesta_Form(forms.Form):
    NroAgente = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'C.I. o R.U.C.',
            },
        ),
    )
    NroCliente = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'C.I. o R.U.C.',
            },
        ),
    )
    NombreCliente = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Completo',
                'readonly': 'True',
            },
        ),
    )
    SectorEconomico = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'True',
            },
        ),
    )
    Telefono = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 0981405221',
                'readonly': 'True',
            },
        ),
    )
    DireccionLibre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'True',
            },
        ),
    )
    Garantia = forms.ChoiceField(
        choices=Garantia,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Moneda = forms.ChoiceField(
        choices=Moneda,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Modalidad = forms.ChoiceField(
        choices=Modalidad,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Destino = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Tasa = forms.CharField(
        max_length=2,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    Comision = forms.DecimalField(
        decimal_places=6,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 00,000000'
            },
        ),
    )


class Cheques(forms.Form):
    Librador = forms.CharField(
        max_length=30,
    )
    Banco = forms.CharField(
        max_length=30
    )
    NroCuenta = forms.CharField(
        max_length=30
    )
    NroCheque = forms.CharField(
        max_length=30
    )
    monto = forms.IntegerField()
    F_Emision = forms.DateField()
    F_Pago = forms.DateField()


ChequesFormsets = formset_factory(
    Cheques,
    extra=1
)
