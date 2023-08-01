from django.db import models
from seguridad.models import ModelBase, ModelBaseAudited


class Cursos(ModelBase):
    id_curso = models.CharField(verbose_name="id_curso", max_length=10, blank=True, null=True)
    nombre_cursos = models.CharField(verbose_name="nombrecurso", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_cursos


    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'Cursos'

class Profesor(ModelBase):
    id_profesor = models.CharField(verbose_name="id_profesor", max_length=10, blank=True, null=True)
    nombre_profesor = models.CharField(verbose_name="nombre_profesor", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_profesor

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'




class grupos(ModelBase):
    id_grupo = models.CharField(verbose_name="id_grupo", max_length=10, blank=True, null=True)
    nombre_grupos = models.CharField(verbose_name="nombregrupos", max_length=100, blank=True, null=True)
    id_profesor = models.ForeignKey(Profesor, verbose_name="Profesor"  ,on_delete=models.CASCADE,blank=True, null=True)
    id_curso = models.ForeignKey(Cursos,verbose_name="Curso" , on_delete=models.CASCADE,blank=True, null=True)



    def __str__(self):
        return self.nombre_grupos

    class Meta:
        verbose_name = 'grupo'
        verbose_name_plural = 'Grupos'


class Alumno(ModelBase):
    id_alumno = models.CharField(verbose_name="id_alumno", max_length=10, blank=True, null=True)
    Nombres = models.CharField(verbose_name="Nombres", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Nombres

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


class Matricula(ModelBase):
    id_matricula = models.CharField(verbose_name="id_matricula", max_length=10, blank=True, null=True)
    id_curso = models.ForeignKey(Cursos, verbose_name="Cursos" ,on_delete=models.CASCADE,blank=True, null=True)
    id_alumno = models.ForeignKey(Alumno, verbose_name="Alumno" , on_delete=models.CASCADE,blank=True, null=True)



    def __str__(self):
        return self.id_matricula

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'


class AlumnoenGrupo(ModelBase):
    id_alumnoengrupo = models.CharField(verbose_name="id_alumnogrupo", max_length=10, blank=True, null=True)
    id_matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.id_alumnoengrupo

    class Meta:
        verbose_name = 'Alumno en grupo'
        verbose_name_plural = 'Alumnos  en grupos'

class Tipocancelacion(ModelBase):
    id_tripocancelacion = models.CharField(verbose_name="id_tipocancelacion", max_length=10, blank=True, null=True)
    Nombre = models.CharField(verbose_name="Nombre_cancelacion", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'tipo cancelacion'
        verbose_name_plural = 'tipos de cancelacion'



class Horario(ModelBaseAudited):
    Profesor = models.ForeignKey(Profesor, verbose_name="Profesor",on_delete=models.CASCADE,blank=True, null=True)
    Grupo = models.ForeignKey(grupos,verbose_name="Grupo" ,on_delete=models.CASCADE,blank=True, null=True)
    id_horario = models.CharField(verbose_name="Código", max_length=10, blank=True, null=True)
    Horas = models.CharField(verbose_name="Horas", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Horas

    class Meta:
        verbose_name = 'Hora'
        verbose_name_plural = 'Horas'

class Tipotarea(ModelBase):
    id_tarea = models.CharField(verbose_name="id_tipotarea", max_length=10, blank=True, null=True)
    Nombre = models.CharField(verbose_name="Nombretarea", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'tipo tarea'
        verbose_name_plural = 'tipos de tarea'



class Clase(ModelBaseAudited):
    tipo_cancelacion = models.ForeignKey(Tipocancelacion, verbose_name="Cancelacion" ,on_delete=models.CASCADE,blank=True, null=True)
    id_clase = models.CharField(verbose_name="id clase", max_length=10, blank=True, null=True)
    horario = models.ForeignKey(Horario, verbose_name="Horario" ,on_delete=models.CASCADE,blank=True, null=True)
    tipo_tarea = models.ForeignKey(Tipotarea, verbose_name="Tarea" ,on_delete=models.CASCADE,blank=True, null=True)
    id_profesor = models.ForeignKey(Profesor, verbose_name="Profesor" ,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.id_clase

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

class Asistencia(ModelBase):
    id_Asistencia = models.CharField(verbose_name="id_asistencia", max_length=10, blank=True, null=True)
    id_clase = models.ForeignKey(Clase, verbose_name="Clase",on_delete=models.CASCADE,blank=True, null=True)
    id_alumnoengrupo = models.ForeignKey(AlumnoenGrupo, verbose_name="Alumno" , on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.id_Asistencia

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

