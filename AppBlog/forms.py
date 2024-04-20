from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *




class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}



class UserEditForm(UserChangeForm):

    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)
    imagen = forms.ImageField(label="Avatar", required="False")
    
    class Meta:
        model = User
        fields = ['email','password1','password2', 'imagen']
        help_text = {k:"" for k in fields}






class curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()


class alumno_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    curso = forms.CharField(max_length=20)



class profesor_formulario(forms.ModelForm):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    profesion = forms.CharField(max_length=20)
    foto = forms.ImageField(label="foto", required="false")
    class Meta:
        model = Profesor
        fields = ['nombre','apellido','profesion', 'foto']
        help_text = {k:"" for k in fields}




class entregable_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    fecha_de_entrega = forms.DateField()

