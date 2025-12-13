from django.db import models
from django.core.validators import MinLengthValidator

class Departamento(models.Model):
    nombre = models.CharField(
        max_length=80,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre


class Sensor(models.Model):
    ESTADOS = [
        ("ACTIVO", "ACTIVO"),
        ("INACTIVO", "INACTIVO"),
        ("MANTENCION", "MANTENCION"),
    ]

    mac = models.CharField(max_length=17, unique=True)  # ejemplo: AA:BB:CC:DD:EE:FF
    nombre = models.CharField(max_length=80, validators=[MinLengthValidator(3)])
    estado = models.CharField(max_length=12, choices=ESTADOS, default="ACTIVO")
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name="sensores")

    def __str__(self):
        return f"{self.nombre} ({self.mac})"


class Evento(models.Model):
    RESULTADOS = [
        ("PERMITIDO", "PERMITIDO"),
        ("DENEGADO", "DENEGADO"),
    ]

    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, related_name="eventos")
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name="eventos")
    resultado = models.CharField(max_length=10, choices=RESULTADOS)
    detalle = models.CharField(max_length=200, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha_hora} - {self.sensor.mac} - {self.resultado}"


class Barrera(models.Model):
    ESTADOS = [
        ("ABIERTA", "ABIERTA"),
        ("CERRADA", "CERRADA"),
    ]

    departamento = models.OneToOneField(Departamento, on_delete=models.PROTECT, related_name="barrera")
    estado = models.CharField(max_length=10, choices=ESTADOS, default="CERRADA")
    actualizada_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Barrera {self.departamento.nombre} - {self.estado}"
