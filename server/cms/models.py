# Create your models here.
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add custom fields here if needed
    pass

class MenuSubItem2(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def is_parent(self):
        return self.parent is None

    def get_children(self):
        return MenuSubItem2.objects.filter(parent=self)

    
    def get_icon(self):
        return self.icon if self.icon else 'icon-grid' 
    
    
class MedicalEquipment(models.Model):
    EQUIPMENT_TYPES = (
        ('ECG', 'Electrocardiograma'),
        ('BP', 'Monitor de presion sanguinea'),
        ('SP', 'Estetoscopio'),
        ('OT', 'Tanque de oxigeno'),
        # Add more equipment types as needed
    )

    serial_number = models.CharField(max_length=20)
    equipment_type = models.CharField(max_length=4, choices=EQUIPMENT_TYPES)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    calibration_date = models.DateField()
    last_service_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_equipment_type_display()} - {self.serial_number}"


class MedicalEquipments(models.Model):
    estados = (
    ('activo', 'Activo'),
    ('pendiente', 'Pendiente'),
    ('urgente', 'Urgente'),
        # Add more equipment types as needed
    )

    equipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=6)
    no_serie  = models.IntegerField()
    servicio_ult = models.DateField()
    servicio_prox = models.DateField()
    estado = models.CharField(max_length=10, choices=estados)
    area = models.CharField(max_length=50)
    subarea = models.CharField(max_length=50)
    encargado = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.equipo
class MedicalEquipmentDetails(models.Model):

    equipo = models.OneToOneField(
        MedicalEquipments,
        on_delete=models.CASCADE,
        related_name='details'
    )
    
    instalacion_fecha = models.DateField(verbose_name='fecha de instalación')
    anios_operando = models.IntegerField(verbose_name='años operando')
    ultima_actualizacion = models.DateTimeField()
    estatus = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    sub_ubicacion = models.CharField(max_length=200)
    pertenencia = models.CharField(max_length=200)
    duenio = models.CharField(max_length=200, verbose_name='dueño')
    vendido_por = models.CharField(max_length=200)
    adquisicion = models.DateField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
    divisas = models.CharField(max_length=5) 
    provedor = models.CharField(max_length=200)
    frecuencia_mprev = models.CharField(max_length=200)
    ultimo_mprev = models.DateField()
    proximo_mprev = models.DateField()
    riesgo = models.CharField(max_length=200)
    cricticidad = models.CharField(max_length=200)
    provedor = models.CharField(max_length=200)
    garantia = models.CharField(max_length=200)
    accesorios = models.CharField(max_length=200)


    def __str__(self):
        return str(self.equipo)