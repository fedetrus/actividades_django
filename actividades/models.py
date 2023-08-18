from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Actividades(models.Model):
    actividades = models.CharField(max_length=100, verbose_name='Actividad', null=True)

    def __str__(self):
       return str(self.actividades)
    
class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Nro')
    actividad_user = models.ForeignKey(Actividades, on_delete=models.CASCADE, verbose_name='Actividad', null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creado')
    asignador = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Asignado por', null=True, blank=True, related_name='Actividad_asignado_por')
    asginado = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Asignado', null=True, blank=True, related_name='actividades_asignadas_a')
    inicio = models.DateTimeField(verbose_name='Inicio', blank=True, null=True)
    fin = models.DateTimeField(verbose_name='Fin', blank=True, null=True)

    def __str__(self):
       return str(self.actividad_user)
"""
################################################################################
                            Actividades

Id              (00523)
Fecha creación  (Se crea automaticamente con estado de Nuevo)
Actividad       (FK Actividades.actividad)
Inicio          (Fecha y hora de inicio)
Estado          (FK Estados.estado)
Asignado por    (Usuario que asigna la tarea)
Asignado a      (Usuario al cual le fue designada la tarea)
Fin             (Fecha y hora de finalización)
Porcentaje
Tiempo          (Tiempo entre que se dio curso hasta que se finalizó)
Proyecto        (Tag del proyecto)

########################################
                Estados

Estado          (Nuevo, En Espera, En Curso, Pausa, Finalizado, Cerrado)

########################################
                Actividades

Actividad       (Escaneo, Edición, OCR, Redimensionado, Preparado, Destrucción,
                 Armado, Traslado, Carga, Codificación, Visita, Relevamiento...)

########################################
                Prioridades

Prioridad          (Baja, Normal, Alta, Urgente)

################################################################################
"""