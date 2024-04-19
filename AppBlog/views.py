from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from AppBlog.forms import *
from django.contrib.auth.decorators import login_required
from AppBlog.models import Avatar, Entregable, Profesor, Curso, Alumno
from django.template import loader



# Create your views here.

#--------------------------------PAGINAS-------------------------------------------#

def home(request):
    return render(request, "home.html")


def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")




#--------------------------------USUARIO-------------------------------------------#


def login_request(request):

    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
    

            if user is not None:
                
                login(request,user)

                return render(request, "inicio.html", { "mensaje":f"Bienvenido/a {usuario}", "usuario":usuario})
            
            else:
                return HttpResponse("Error, datos incorrectos")
        else:
            return render(request, "login2.html", {"mensaje":f"Ingrese un usuario y contraseña correctos"})

    
    form = AuthenticationForm()
    return render(request,"login.html", {"form":form})




def register(request):
    

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():

            form.save()

            return render(request, "registrado.html", {"mensaje":f"Usuario creado"})
        else:
            return render(request, "registrado.html", {"mensaje":"Error, formulario erroneo" } )

    else:
        form = UserRegisterForm()

    return render(request,"registro.html", {"form":form})



def user_logout(request):
    logout(request)
    return render(request, 'logout.html', {})



def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST, request.FILES, instance = request.user)

        if mi_formulario.is_valid():
            
            if mi_formulario.cleaned_data.get('imagen'):
                
                datos = mi_formulario.cleaned_data
                usuario.avatar.imagen = mi_formulario.cleaned_data.get('imagen')
                usuario.avatar.save()

            mi_formulario.save()


            return render(request , "inicio.html", {"mensaje":f"Perfil actualizado", "usuario":usuario } )

    else:
        miFormulario = UserEditForm(initial={"imagen": "AppBlog/static/AppBlog/assets/me.png"}, instance=request.user)
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})




def inicio(request):
    usuario = request.user
    return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}", "usuario":usuario })







#--------------------------------PROFESORES-------------------------------------------#



def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "profesores.html", {"profesores" : profesores})



def Profesor_formulario(request):


    if request.method == "POST":
        mi_formulario = profesor_formulario(request.POST, request.FILES)

        if mi_formulario.is_valid():
        
            datos = mi_formulario.cleaned_data
            
            profesor = Profesor(nombre=datos["nombre"] , apellido=datos["apellido"], profesion=datos["profesion"], foto=datos["foto"])
                

            profesor.save()

            return render(request , "agregado.html", {"mensaje":f"Profesor {profesor.nombre} {profesor.apellido} añadido"})
    

    return render(request , "formulario_profesor.html", {"mensaje":"Agregar profesor"}, )





def  buscarProfesor(request):

        if request.GET["nombre"]:
            nombre = request.GET["nombre"]
            profesores = Profesor.objects.filter(nombre__icontains= nombre)
            return render(request , "resultado_busqueda_profesor.html" , {"profesores":profesores})
        else:
            print("Profesor no encontrado")
            


def elimina_profesor(request , id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesor = Profesor.objects.all()

    return render(request , "profesores.html" , {"profesores":profesor})



def editarProfesor(request, profesor_nombre):


    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == "POST":
        
        mi_formulario = profesor_formulario(request.POST, request.FILES)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            profesor.nombre= informacion['nombre']
            profesor.apellido= informacion['apellido']
            profesor.profesion= informacion['profesion']

            if mi_formulario.cleaned_data.get('imagen'):

                profesor.Foto.foto = mi_formulario.cleaned_data.get('imagen')
                profesor.foto.save()

            profesor.save()



            return render(request , "agregado.html", {"mensaje":f"Profesor {profesor.nombre} {profesor.apellido} actualizado", "profesor_nombre":profesor_nombre } )

    else:
        miFormulario = profesor_formulario(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "profesion": profesor.profesion})
    
    return render( request , "formulario_profesor.html", {"mensaje":f"Editar al profesor {profesor.nombre} {profesor.apellido}", "miFormulario":miFormulario, "profesor_nombre":profesor_nombre})




#--------------------------------ALUMNOS-------------------------------------------#



def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "alumnos.html", {"alumnos" : alumnos})



def Alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = alumno_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre=datos["nombre"] , apellido=datos["apellido"], curso=datos["curso"])
            alumno.save()
            return render(request , "agregado.html", {"mensaje":f"Alumno {alumno.nombre} {alumno.apellido} añadido", "alumno":alumno.nombre })


    return render (request , "formulario_alumno.html", {"mensaje":f"Agregar alumno"})




def  buscarAlumno(request):

        if request.GET["nombre"]:

            nombre = request.GET["nombre"]
            alumnos = Alumno.objects.filter(nombre__icontains= nombre)
            return render(request , "resultado_busqueda_alumno.html" , {"alumnos":alumnos})
            
        else:
        
            print("Alumno no encontrado")





def elimina_alumno(request , id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno = Alumno.objects.all()

    return render(request , "alumnos.html" , {"alumnos":alumno})




def editarAlumno(request, alumno_nombre):

    alumno = Alumno.objects.get(nombre=alumno_nombre)

    if request.method == "POST":
        
        mi_formulario = alumno_formulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            alumno.nombre= informacion['nombre']
            alumno.apellido= informacion['apellido']
            alumno.curso= informacion['curso']

            alumno.save()



            return render(request , "agregado.html", {"mensaje":f"Alumno {alumno.nombre} {alumno.apellido} actualizado", "profesor_nombre":alumno_nombre } )

    else:
        miFormulario = alumno_formulario(initial={"nombre": alumno.nombre, "apellido": alumno.apellido, "curso": alumno.curso})
    
    return render( request , "formulario_alumno.html", {"mensaje": f"Editar alumno {alumno.nombre} {alumno.apellido}"})



#--------------------------------CURSOS-------------------------------------------#







def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos" : cursos})



def Curso_formulario(request):

    if request.method == "POST":

        mi_formulario = curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "agregado.html", {"mensaje":f"Curso {curso.nombre} añadido"})


    return render(request , "formulario_curso.html",{"mensaje":"Agregar curso"})




def  buscarCurso(request):

        if request.GET["nombre"]:

            nombre = request.GET["nombre"]
            cursos = Curso.objects.filter(nombre__icontains= nombre)
            return render(request , "resultado_busqueda_alumno.html" , {"cursos":cursos})
            
        else:
        
            print("Curso no encontrado")
    


def elimina_curso(request , id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})



def editarCurso(request, curso_nombre):

    curso = Curso.objects.get(nombre=curso_nombre)

    if request.method == "POST":
        
        mi_formulario = curso_formulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            curso.nombre= informacion['nombre']
            curso.camada= informacion['camada']

            curso.save()



            return render(request , "agregado.html", {"mensaje":f"Curso {curso.nombre} actualizado", "cuurso_nombre":curso_nombre } )

    else:
        miFormulario = curso_formulario(initial={"nombre": curso.nombre, "camada": curso.camada})
    
    return render( request , "formulario_curso.html", {"mensaje":f"Editar curso {curso.nombre}", "miFormulario":miFormulario, "curso_nombre":curso_nombre})



#--------------------------------ENTREGABLES-------------------------------------------#




def ver_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, "entregables.html", {"entregables" : entregables})



def Entregable_formulario(request):
    if request.method == "POST":
        mi_formulario = entregable_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            entregable = Entregable(nombre=datos["nombre"] , fecha_de_entrega=datos["fecha_de_entrega"])
            entregable.save()
            return render(request , "agregado.html", {"mensaje": f"Entregable {entregable.nombre} agregado"})


    return render (request , "formulario_entregable.html", {"mensaje":"Agregar entregable"})





def  buscarEntregable(request):
        
        if request.GET["nombre"]:
            nombre = request.GET["nombre"]
            entregables = Entregable.objects.filter(nombre__icontains= nombre)
            return render(request , "resultado_busqueda_entregable.html" , {"entregables":entregables})
        else:
            print("Entregable no encontrado")



def elimina_entregable(request , id):
    entregable = Entregable.objects.get(id=id)
    entregable.delete()

    entregable = Entregable.objects.all()

    return render(request , "entregables.html" , {"entregables":entregable})




def editarEntregable(request, entregable_nombre):

    entregable = Entregable.objects.get(nombre=entregable_nombre)

    if request.method == "POST":
        
        mi_formulario = entregable_formulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            entregable.nombre= informacion['nombre']
            entregable.fecha_de_entrega= informacion['fecha_de_entrega']

            entregable.save()



            return render(request , "agregado.html", {"mensaje":f"Entregable {entregable.nombre} actualizado", "entregable_nombre":entregable_nombre } )

    else:
        miFormulario = entregable_formulario(initial={"nombre": entregable.nombre, "fecha_de_entrega": entregable.fecha_de_entrega})
    
    return render( request , "formulario_entregable.html", {"mensaje":f"Editar entregable {entregable.nombre}", "miFormulario":miFormulario, "entregable_nombre":entregable_nombre})







