from django.contrib import admin
from .models import Actividad, ActividadTipo, Estado

# Register your models here.

admin.site.register(Actividad)
admin.site.register(ActividadTipo)
admin.site.register(Estado)