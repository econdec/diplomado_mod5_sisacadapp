from django.urls import include, path
from rest_framework.routers import DefaultRouter

#from . import views
from .views import AlumnoViewSet, MateriaViewSet, NotaViewSet

from . import views

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('alumnos/cantidad/', views.alumno_count, name='alumno-cantidad'),
    path('alumnos/reporte/', views.alumno_reporte, name='alumno-reporte'),
    path('', include(router.urls)),
]