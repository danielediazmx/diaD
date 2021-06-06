from django.db import models


# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200, blank=True)
    apellido_materno = models.CharField(max_length=200, blank=True)
    municipio = models.CharField(max_length=100)
    celular = models.CharField(max_length=30)
    coordinacion = models.CharField(max_length=50)

    invitado_por = models.CharField(max_length=200)

    ya_voto = models.BooleanField(default=False)

    def red(self):
        return "ISEA"

    def calcularMisInvitados(self):
        mis_invitados = Registro.objects.filter(
            invitado_por=self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno)
        return mis_invitados.count()

    def tengoInvitados(self):
        return bool(self.calcularMisInvitados())
