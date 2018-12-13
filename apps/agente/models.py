from django.db import models


class Agente(models.Model):
    idAgente = models.AutoField(primary_key=True)
    NroDocumento = models.CharField(
        max_length=7,
        unique=True,
    )
    Apellido = models.CharField(
        max_length=30
    )
    Nombre = models.CharField(
        max_length=30
    )

    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'

    def __str__(self):
        return "%s %s" % (self.Apellido, self.Nombre)
