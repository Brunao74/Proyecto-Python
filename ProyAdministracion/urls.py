#Bruno Rossi

from django.urls import path
from . import views
from ProyAdministracion.models import Curso, Alumno, BandaHoraria
from ProyAdministracion.views import cargar_alumnos, listar_alumnos, obtener_alumno_csv, modificar_alumno, eliminar_alumno, asignar_curso, alumnos_por_curso

#Puntos D al I

urlpatterns = [
    path('cargarAlumnos/', cargar_alumnos, name='cargar_alumnos'),
    path('listarAlumnos/', listar_alumnos, name='listar_alumnos'),
    path('alumno/', obtener_alumno_csv, name='obtener_alumno_csv'),
    path('modificarAlumno/', modificar_alumno, name='modificar_alumno'),
    path('eliminarAlumno/<int:dni>/', eliminar_alumno, name='eliminar_alumno'),
    path('asignarCurso/', asignar_curso, name='asignar_curso'),
    path('alumnosPorCurso/', alumnos_por_curso, name='alumnos_por_curso'),
]
