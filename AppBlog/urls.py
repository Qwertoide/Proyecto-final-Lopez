from . import views
from django.urls import path



urlpatterns = [

    path('', views.home , name='home'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),


    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name="logout"),
    path('editarPerfil/', views.editarPerfil,  name='editarPerfil'),
    path('inicio/', views.inicio,  name='inicio'),


    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("alta_curso", views.Curso_formulario, name="alta_curso"),
    path("buscarCurso", views.buscarCurso),
    path("elimina_curso/<int:id>", views.elimina_curso , name="elimina_curso"),
    path("editarCurso/<curso_nombre>", views.editarCurso , name="editarCurso"),

    path("alumnos", views.ver_alumnos , name="alumnos"),
    path("alta_alumno", views.Alumno_formulario, name="alta_alumno"),
    path("buscarAlumno", views.buscarAlumno),
    path("elimina_alumno/<int:id>", views.elimina_alumno , name="elimina_alumno"),
    path("editarAlumno/<alumno_nombre>", views.editarAlumno , name="editarAlumno"),

    path("profesores", views.ver_profesores , name="profesores"),
    path("alta_profesor", views.Profesor_formulario, name="alta_profesor"),
    path("buscarProfesor", views.buscarProfesor),
    path("editar_profesores", views.editarProfesor , name="editar_profesores"),
    path("elimina_profesor/<int:id>", views.elimina_profesor , name="elimina_profesor"),
    path("editarProfesor/<profesor_nombre>", views.editarProfesor , name="editarProfesor"),

    path("entregables", views.ver_entregables , name="entregables"),
    path("alta_entregable", views.Entregable_formulario, name="alta_entregable"),
    path("buscarEntregable", views.buscarEntregable),
    path("elimina_entregable/<int:id>", views.elimina_entregable , name="elimina_entregable"),
    path("editarEntregable/<entregable_nombre>", views.editarEntregable , name="editarEntregable"),

]

