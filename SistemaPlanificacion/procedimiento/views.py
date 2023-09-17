from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from procedimiento.models import ProductoAcademico,Asignatura,Referencias,Trabajador,Contenido,Responsable,Unidad,Responsable
from django.shortcuts import render

def login(request):
    if request.method == "POST":
        usuarioInput = request.POST["usuario"]
        claveInput = request.POST["clave"]
        try:
            objTrabajador = Trabajador.objects.get(usuario=usuarioInput,estado='A')
        
            if object:
                if objTrabajador.clave == claveInput:
                    return redirect('inicio')
                else:
                    msg = "Credenciales Invalidas vu"
        except:
            msg = "Este usuario no esta registrado en nuestra base de datos"
            
    return render(request,'login.html',{
        'msg':msg
    })
def home(request):
    return render(request,'core.html',{})

def trabajador(request):
    if(request.method == "POST"):
        cedula = request.POST["cedula"] 
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        perfil = request.POST["perfil"]
        objTrabajador = Trabajador(cedula=cedula,nombres=nombres,apellidos=apellidos,usuario=cedula,clave=cedula,perfil=perfil)
        objTrabajador.save()

    return render(request,'añadir-trabajador',{})


def unidad(request):
    asignatura = Asignatura.objects.filter(estado='A')   
    unidad = Unidad.objects.filter(estado='A')
    
    if request.method == "POST":
        vnumero = request.POST["numero"]
        vnombre = request.POST["nombre"]
        vobjetivo = request.POST["objetivo"]
        vasignatura = get_object_or_404(Asignatura,id=int(request.POST["asignatura"]))
        objUnidad = Unidad(
            numero=vnumero,
            nombre = vnombre,
            objetivo=vobjetivo,
            id_asignatura = vasignatura)
        objUnidad.save()
        
    return render(request,'añadir-unidad',{
        'asignatura':asignatura,
        'unidad':unidad,
        
        })

def contenido(request):
    unidad = Unidad.objects.filter(estado='A')
    tablascontenido = Contenido.objects.filter(estado='A')
       
    if (request.method == "POST"):
        vnumero = request.POST["numero"]
        vcontenido = request.POST["contenido"]
        vhoras_docencia = request.POST["horas-docencia"]
        vminutos_practicas = request.POST["horas-docencia"]
        vhoras_gestion = request.POST["horas-gestion"]
        vhoras_autonomas = request.POST["horas-autonomas"]
        vunidad = get_object_or_404(Unidad,id=int(request.POST["unidad"]))    
        
        objcontenido = Contenido(numero=vnumero,
                                 contenido=vcontenido,
                                 horas_docencia=vhoras_docencia,
                                 minutos_practica=vminutos_practicas,
                                 horas_gestion=vhoras_gestion,
                                 horas_autonomas=vhoras_autonomas,
                                 id_unidad=vunidad)
              
        objcontenido.save()

    return render(request,'añadir-contenido',{
        'unidad':unidad,
        'contenido':tablascontenido,
    })

def firma(request):
    asignatura = Asignatura.objects.filter(estado='A')
    usuarios = Trabajador.objects.filter(estado='A')
    objresponsable = Responsable.objects.filter(estado='A')
    if request.method == "POST":
        responsable_id = request.POST.get("responsable")
        asignatura_id = request.POST.get("asignatura")  
        if responsable_id and asignatura_id:
            vresponsable = get_object_or_404(Trabajador, id=int(responsable_id))
            vasignatura = get_object_or_404(Asignatura, id=int(asignatura_id))
            obj = Responsable(firma="",id_trabajador=vresponsable,id_asignatura=vasignatura)
            obj.save()
            
    return render(request,'añadir-firmas',{
        'asignatura':asignatura,
        'usuarios':usuarios,
        'responsable':objresponsable})

def asignatura(request):
    if(request.method == "POST"):
        datos = []
        for i in request.POST:
            datos.append(request.POST.get(i))
        datos.pop(0)
        objasignatura = Asignatura(
            nombre=datos[0],
            objetivos=datos[1],
            aportesTeoricos=datos[2],
            objetivosEspecificos=datos[3],
            descripcionProducto=datos[4],
            prerequisitos=datos[5],
            periodo=datos[6],
            metodosEnsenanza=datos[7],
            medios=datos[8],
            evaluacion=datos[9]
        )
        
        objasignatura.save()

    return render(request,'añadir-asignatura',{})

def productoAcademico(request):
    asignatura = Asignatura.objects.filter(estado='A')
    datosProducto = ProductoAcademico.objects.filter(estado="A")
    msg = ""
    
    if request.method == "POST":

        if "crear" in request.POST:
            vobjetivo = request.POST["objetivos"]
            vproducto_parcial = request.POST["productoParciales"]
            vresultado_estandares = request.POST["resultadoEstandares"]
            vintegracion_carreras = request.POST["integracionCarrera"]
            vid_asignatura = get_object_or_404(Asignatura, id=int(request.POST["asignatura"]))
            objDP = ProductoAcademico(
                objetivo=vobjetivo,
                producto_parcial=vproducto_parcial,
                resultado_estandares=vresultado_estandares,
                integracion_carreras=vintegracion_carreras,
                id_asignatura=vid_asignatura
            )    
            objDP.save()
            msg = True
        elif "eliminar" in request.POST:
            update = ProductoAcademico.objects.get(id=request.POST["eliminar"])
            update.estado = "I"
            update.save()
            
    return render(request, 'añadir-producto-academico', {  
        'datosProducto': datosProducto,
        'asignatura': asignatura,
        "msg": msg
    })

def referencias(request):
    asignatura = Asignatura.objects.filter(estado='A')   
    datosReferencias = Referencias.objects.filter(estado='A')
    if(request.method == "POST"):
        if "crear" in request.POST: 
            tipoReferencia = request.POST["tipoReferencia"]
            numero = request.POST["numero"]
            descripcion = request.POST["descripcion"]
            biblioteca = request.POST["biblioteca"]
            numerosEjemplares = request.POST["numerosEjemplares"]
            print(request.POST["asignatura"])
            vid_asignatura = get_object_or_404(Asignatura, id=int(request.POST["asignatura"]))

            if(biblioteca == "verdadero"):
                biblioteca = True
            else:
                biblioteca = False

            nueva_referencia = Referencias(numero=numero,
                                           descripcion=descripcion,
                                           Biblioteca=biblioteca,
                                           numerosEjemplares=numerosEjemplares,
                                           tipo=tipoReferencia,
                                           id_asignatura=vid_asignatura)
            nueva_referencia.save()
            
            msg = True
        elif "eliminar" in request.POST:
            update = Referencias.objects.get(id=request.POST["eliminar"])
            update.estado = "I"
            update.save()
        
            
    return render(request,'añadir-referencias',{'referencia':datosReferencias,'asignatura':asignatura})

def subirPlantilla(request):
    dcon = {}
    datosContenido = []
    productoAcademico = None
    referencias = None
    tabla = None
    objunidades = None
    objcontenido = None
    firmas= None
    datosasignatura = Asignatura.objects.filter(estado='A')
    
    if request.method == "POST":
        if "adjuntar" in request.POST:
            asignatura = Asignatura.objects.get(id=int(request.POST["asignatura"]))#Obtener solo una instacion 
            productoAcademico = ProductoAcademico.objects.filter(id_asignatura=asignatura.id,estado='A')
            referencias = Referencias.objects.filter(id_asignatura=asignatura.id,estado='A')
            tabla = asignatura
            objunidades = Unidad.objects.filter(id_asignatura=asignatura,estado="A")
            objcontenido = Contenido.objects.filter(Q(id_unidad__id_asignatura__nombre=asignatura.nombre) &
                                        Q(id_unidad__estado='A'))
            listaObjetos = []
            firmas = Responsable.objects.filter(id_asignatura=asignatura,estado="A")
            for i in objcontenido:
                n = i.id_unidad
                if n is not dcon:
                    dcon[n] = []
                listaObjetos.append(i) 
            for i in dcon:                
                datosContenido.append(Contenido.objects.filter(id_unidad=i.id))
        
    return render(request,'subir-plantilla',{'asignatura':datosasignatura,
                                             'productoAcademico':productoAcademico,
                                             'referencia':referencias,
                                             'tabla':tabla,
                                             'unidad':objunidades,
                                             'contenido':dcon,
                                             'responsable':firmas,
                                             'prueba':datosContenido})
