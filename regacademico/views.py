#from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


#from .forms import ProductoForm
from .models import Alumno, Materia, Inscripcion, Nota
from .serializers import (AlumnoSerializer, MateriaSerializer,
                          InscripcionSerializer, NotaSerializer)


# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

def alumnoFormView(request):
    form = AlumnoForm
    alumno = None

    id_alumno = request.GET.get('id')
    if id_alumno:
        alumno = get_object_or_404(Alumno, id=id_alumno)
        form = AlumnoForm(instance=alumno)

    if request.method == 'POST':
        if alumno:
            form = AlumnoForm(request.POST, instance=alumno)
        else:
            form = AlumnoForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'form_alumnos.html', {
        "form": form
    })

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

@api_view(['GET'])
def alumno_count(request):
    try:
        cantidad = Alumno.objects.count()
        return JsonResponse({
                'cantidad': cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

@api_view(['GET'])
def alumno_reporte(request):
    try:
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data, status=200)
        
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)