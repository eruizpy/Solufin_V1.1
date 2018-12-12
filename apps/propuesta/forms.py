from django import forms
from django.forms import formset_factory
from apps.propuesta.choices import *


class Propuesta_Form(forms.Form):
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
            },
        ),
    )
    SectorEconomico = forms.CharField(
        max_length=30,
    )
    Telefono = forms.CharField(
        max_length=10,
    )
    DireccionLibre = forms.CharField(
        max_length=30
    )
    Garantia = forms.ChoiceField(
        choices=Garantia,
    )
    Moneda = forms.ChoiceField(
        choices=Moneda
    )
    Modalidad = forms.ChoiceField(
        choices=Modalidad
    )
    Destino = forms.CharField(
        max_length=30
    )
    Tasa = forms.CharField(
        max_length=2
    )
    Comision = forms.DecimalField(
        decimal_places=6
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
