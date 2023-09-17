from django.db import models

# Create your models here.º



class Trabajador(models.Model):
    cedula = models.CharField(max_length=15,unique=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    usuario = models.CharField(max_length=150, unique=True)
    clave = models.CharField(max_length=150)
    perfil = models.CharField(max_length=150)
    estado = models.CharField(max_length=3,default='A')
    

class Asignatura(models.Model):
    nombre = models.CharField(max_length=500)
    objetivos = models.TextField()
    aportesTeoricos = models.TextField()
    objetivosEspecificos = models.TextField()
    descripcionProducto = models.TextField()
    prerequisitos = models.TextField()
    periodo = models.CharField(max_length=250)
    metodosEnsenanza = models.TextField()
    medios = models.TextField()
    evaluacion = models.TextField()
    estado = models.CharField(max_length=3,default='A')
    
class ProductoAcademico(models.Model):
    objetivo = models.TextField()
    producto_parcial = models.TextField()
    resultado_estandares = models.TextField()
    integracion_carreras = models.TextField()
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3,default='A')

class Referencias(models.Model):
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    Biblioteca = models.BooleanField()
    numerosEjemplares = models.IntegerField()
    tipo = models.CharField(max_length=250)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3,default='A')
    


class Responsable(models.Model):
    firma = models.CharField(max_length=800)
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3,default='A')

class Unidad(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=150)
    objetivo = models.TextField()
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3,default='A')


class Contenido(models.Model):
    numero = models.IntegerField()
    contenido = models.CharField(max_length=500)
    horas_docencia = models.IntegerField()
    minutos_practica = models.IntegerField()
    horas_gestion = models.IntegerField()
    horas_autonomas = models.IntegerField()
    id_unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3,default='A')