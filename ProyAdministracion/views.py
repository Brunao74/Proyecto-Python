#Bruno Rossi

import csv
import json
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Alumno, Curso, BandaHoraria

@csrf_exempt  # Desactiva la protección CSRF para este ejemplo. Debes manejar CSRF de manera adecuada en un entorno de producción.

#Punto D

def cargar_alumnos(request):
    if request.method == 'POST' and request.FILES['archivo']:
        archivo_csv = request.FILES['archivo']

        # Lee el archivo CSV y crea instancias de Alumno
        with archivo_csv.open(mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                dni = int(row['DNI'])
                # Verifica si el alumno ya existe antes de guardarlo
                if not Alumno.objects.filter(dni=dni).exists():
                    Alumno.objects.create(
                        nombre=row['Nombre'],
                        apellido=row['Apellido'],
                        dni=dni,
                        telefono=row['Teléfono'],
                        correo_electronico=row['Correo Electrónico'],
                        curso_id=int(row['Curso'])
                    )

        return HttpResponse('Alumnos cargados exitosamente.')

    return render(request, 'cargar_alumnos.html')  # Necesitarás crear esta plantilla

#Punto E
def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'listar_alumnos.html', {'alumnos': alumnos})

#Punto F
def obtener_alumno_csv(request):
    if 'dni' in request.GET:
        dni = request.GET['dni']
        alumno = get_object_or_404(Alumno, dni=dni)

        # Crear la respuesta en formato CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{alumno.nombre}_{alumno.apellido}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Nombre', 'Apellido', 'DNI', 'Teléfono', 'Correo Electrónico', 'Curso', 'Banda Horaria'])
        writer.writerow([alumno.nombre, alumno.apellido, alumno.dni, alumno.telefono, alumno.correo_electronico, alumno.curso.nombre, alumno.curso.banda_horaria.nombre])

        return response

    return HttpResponse('Parámetro DNI no proporcionado.')

#Punto G
def modificar_alumno(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
            dni = data.get('dni')
            nuevo_nombre = data.get('nombre')
            nuevo_apellido = data.get('apellido')
            nuevo_telefono = data.get('telefono')
            nuevo_correo = data.get('correo_electronico')
            nuevo_curso_id = data.get('curso')

            # Verifica que el alumno exista
            alumno = get_object_or_404(Alumno, dni=dni)

            # Actualiza los datos del alumno
            alumno.nombre = nuevo_nombre if nuevo_nombre else alumno.nombre
            alumno.apellido = nuevo_apellido if nuevo_apellido else alumno.apellido
            alumno.telefono = nuevo_telefono if nuevo_telefono else alumno.telefono
            alumno.correo_electronico = nuevo_correo if nuevo_correo else alumno.correo_electronico
            alumno.curso_id = nuevo_curso_id if nuevo_curso_id else alumno.curso_id

            # Guarda los cambios
            alumno.save()

            return JsonResponse({'mensaje': 'Alumno modificado correctamente'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)

    return JsonResponse({'error': 'Método HTTP no permitido'}, status=405)

#Punto H
def eliminar_alumno(request, dni):
    if request.method == 'DELETE':
        # Verifica que el alumno exista
        alumno = get_object_or_404(Alumno, dni=dni)

        # Elimina el alumno
        alumno.delete()

        return JsonResponse({'mensaje': 'Alumno eliminado correctamente'})

    return JsonResponse({'error': 'Método HTTP no permitido'}, status=405)

#Punto I
def asignar_curso(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            dni = data.get('dni')
            curso_id = data.get('curso_id')

            # Verifica que el alumno y el curso existan
            alumno = get_object_or_404(Alumno, dni=dni)
            curso = get_object_or_404(Curso, id=curso_id)

            # Asigna el nuevo curso al alumno
            alumno.curso = curso
            alumno.save()

            return JsonResponse({'mensaje': 'Curso asignado correctamente'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)

    return JsonResponse({'error': 'Método HTTP no permitido'}, status=405)

#Punto J
def alumnos_por_curso(request):
    if 'curso_id' in request.GET:
        curso_id = request.GET['curso_id']

        # Verifica que el curso exista
        get_object_or_404(Curso, id=curso_id)

        # Consulta los alumnos del curso
        alumnos = Alumno.objects.filter(curso_id=curso_id)

        # Formatea la información de los alumnos en formato JSON
        alumnos_info = []
        for alumno in alumnos:
            alumnos_info.append({
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'dni': alumno.dni,
                'telefono': alumno.telefono,
                'correo_electronico': alumno.correo_electronico,
            })

        return JsonResponse({'alumnos': alumnos_info})

    return JsonResponse({'error': 'Parámetro curso_id no proporcionado.'}, status=400)
