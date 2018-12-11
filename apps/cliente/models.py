from django.db import models
from apps.cliente.choices import *
from django.contrib.auth import get_user_model
from django.conf import settings
UserModel = get_user_model()


class Cliente(models.Model):
    Usuario = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    idCliente = models.AutoField(primary_key=True)
    SectorEconomico = models.PositiveSmallIntegerField(
        choices=SectoresEconomicos,
    )
    TipoPersona = models.PositiveSmallIntegerField(
        choices=TipoPersona,
    )
    PaisDoc = models.CharField(max_length=2, choices=PaisDoc)
    TipoDocumento = models.PositiveSmallIntegerField(
        choices=TipoDoc,
    )
    NumeroDocumento = models.CharField(
        max_length=10,
        unique=True,
    )
    Apellido = models.CharField(
        max_length=30,
    )
    Nombre = models.CharField(
        max_length=30,
    )
    NombreCompleto = models.CharField(
        max_length=60,
    )
    FechaNacimiento = models.DateField()
    Genero = models.CharField(
        max_length=1,
        choices=Generos,
    )
    EstadoCivil = models.PositiveSmallIntegerField(
        choices=EstadoCivil,
    )
    Nacionalidad = models.CharField(
        max_length=2,
        choices=Nacionalidad,
    )
    Telefono = models.CharField(max_length=10)
    TipoDireccion = models.PositiveSmallIntegerField(
        choices=TipoDireccion,
    )
    Pais = models.CharField(
        max_length=2,
        choices=Pais,
    )
    Departamento = models.CharField(
        max_length=3,
        choices=Departamentos,
    )
    Ciudad = models.CharField(max_length=30)
    Bario = models.CharField(max_length=30)
    DireccionLibre = models.CharField(max_length=255)
    ComprobanteIngreso = models.CharField(max_length=30)
    Salario = models.CharField(max_length=10)
    CargoTrabajo = models.CharField(max_length=30)
    Dependiente = models.PositiveSmallIntegerField(
        choices=EsDependiente,
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return "%s" % self.NombreCompleto

    def get_NombreCompleto(self):
        return "%s" % self.NombreCompleto
