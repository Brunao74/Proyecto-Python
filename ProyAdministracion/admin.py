#Bruno Rossi

from django.contrib import admin
from .models import Alumno, Curso, BandaHoraria

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(BandaHoraria)
