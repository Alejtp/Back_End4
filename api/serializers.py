import re
from rest_framework import serializers
from .models import Departamento, Sensor, Evento, Barrera

MAC_RE = re.compile(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$")

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

    def validate_mac(self, value):
        value = value.strip().upper()
        if not MAC_RE.match(value):
            raise serializers.ValidationError("MAC inválida. Formato esperado: AA:BB:CC:DD:EE:FF")
        return value

    def validate_nombre(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value.strip()


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"

    def validate(self, attrs):
        # Reglas simples: el evento debe apuntar al mismo departamento del sensor
        sensor = attrs.get("sensor")
        depto = attrs.get("departamento")
        if sensor and depto and sensor.departamento_id != depto.id:
            raise serializers.ValidationError("El departamento del evento debe coincidir con el del sensor.")
        return attrs


class BarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrera
        fields = "__all__"
