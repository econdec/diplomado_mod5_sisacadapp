from django.contrib import admin

from .models import Alumno, Materia, Inscripcion, Nota



class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'ci', 'email', 'fecha_ingreso', 'estado')
    ordering = ('apellido', 'nombre',)
    search_fields = ('ci',)
    list_filter = ('estado',)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_alumno_nombre', 'get_materia_nombre', 'gestion')
    search_fields = ('alumno__apellido', 'materia__nombre')
    list_filter = ('materia',)

    def get_alumno_nombre(self, obj):
        return f"{obj.alumno.nombre} {obj.alumno.apellido}"
    get_alumno_nombre.short_description = 'Alumno'

    def get_materia_nombre(self, obj):
        return obj.materia.nombre
    get_materia_nombre.short_description = 'Materia'

class NotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_alumno', 'get_materia', 'nota')    
    search_fields = ('inscripcion__alumno__apellido', 'inscripcion__materia__nombre')
    list_filter = ('inscripcion__materia',)

    def get_alumno(self, obj):
        return f"{obj.inscripcion.alumno.nombre} {obj.inscripcion.alumno.apellido}"
    get_alumno.short_description = 'Alumno'

    def get_materia(self, obj):
        return obj.inscripcion.materia.nombre
    get_materia.short_description = 'Materia'

admin.site.register(Alumno, AlumnoAdmin)

admin.site.register(Materia, MateriaAdmin)

admin.site.register(Inscripcion, InscripcionAdmin)

admin.site.register(Nota, NotaAdmin)