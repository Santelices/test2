from django.contrib import admin
from .models import *
# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    list_display = (
        'id_curso',
        'nombre_cursos',
    )
    list_per_page = 10
    search_fields = ('id_curso','nombre_cursos')
    list_filter = (
        'nombre_cursos',
    )

admin.site.register(Cursos,CursosAdmin)


class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        'id_profesor',
        'nombre_profesor',
    )
    list_per_page = 10
    search_fields = ('id_profesor','nombre_profesor')
    list_filter = (
        'nombre_profesor',
    )

admin.site.register(Profesor,ProfesorAdmin)

class gruposAdmin(admin.ModelAdmin):
    list_display = (
        'id_grupo',
        'nombre_grupos',
        'id_profesor',
        'id_curso'
    )
    list_per_page = 10
    search_fields = ('id_grupo','nombre_grupos')
    list_filter = (
        'nombre_grupos',
    )

admin.site.register(grupos,gruposAdmin)

class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'id_alumno',
        'Nombres',
    )
    list_per_page = 10
    search_fields = ('id_alumno','Nombres')
    list_filter = (
        'Nombres',
    )

admin.site.register(Alumno,AlumnoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'id_matricula',
        'id_curso',
        'id_alumno'
    )
    list_per_page = 10
    search_fields = ('id_matricula','id_curso','id_alumno')
    list_filter = (
        'id_curso',
    )

admin.site.register(Matricula,MatriculaAdmin)

class AlumnoenGrupoAdmin(admin.ModelAdmin):
    list_display = (
        'id_alumnoengrupo',
        'id_matricula',
        
    )
    list_per_page = 10
    search_fields = ('id_alumnoengrupo','id_matricula')
    list_filter = (
        'id_alumnoengrupo',
    )

admin.site.register(AlumnoenGrupo,AlumnoenGrupoAdmin)

class TipocancelacionAdmin(admin.ModelAdmin):
    list_display = (
        'id_tripocancelacion',
        'Nombre',
        
    )
    list_per_page = 10
    search_fields = ('id_tripocancelacion','Nombre')
    list_filter = (
        'Nombre',
    )

admin.site.register(Tipocancelacion,TipocancelacionAdmin)

class HorarioAdmin(admin.ModelAdmin):
    list_display = (
        'id_horario' ,
        'Horas' ,
        'Profesor',
        'Grupo',
        
    )
    list_per_page = 10
    search_fields = ('id_horario','Horas')
    list_filter = (
        'Profesor',
        'Grupo'
    )

admin.site.register(Horario,HorarioAdmin)

class TipotareaAdmin(admin.ModelAdmin):
    list_display = (
        'id_tarea' ,
        'Nombre' ,
        
    )
    list_per_page = 10
    search_fields = ('id_tarea','Nombre')
    list_filter = (
        'Nombre',
    )

admin.site.register(Tipotarea,TipotareaAdmin)


class ClaseAdmin(admin.ModelAdmin):
    list_display = (
        'id_clase' ,
        'tipo_cancelacion' ,
        'horario',
        'tipo_tarea',
        'id_profesor'
        
    )
    list_per_page = 10
    search_fields = ('id_clase','horario','tipo_tarea')
    list_filter = (
        'horario',
    )

admin.site.register(Clase,ClaseAdmin)


class AsistenciaAdmin(admin.ModelAdmin):
    list_display = (
        'id_Asistencia' ,
        'id_clase' ,
        'id_alumnoengrupo'
        
    )
    list_per_page = 10
    search_fields = ('id_tarea','Nombre')
    list_filter = (
        'id_Asistencia',
    )

admin.site.register(Asistencia,AsistenciaAdmin)

