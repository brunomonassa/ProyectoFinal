from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VentaForm(forms.Form):

    ubicacion = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    precio = forms.IntegerField()
    habitaciones = forms.IntegerField()

class AlquilerForm(forms.Form):

    ubicacion = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    precio = forms.IntegerField()
    habitaciones = forms.IntegerField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label= 'Usuario')
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget= forms.PasswordInput)
    last_name = forms.CharField(label= 'Apellido')
    first_name = forms.CharField(label= 'Nombre')

    class Meta:

        model= User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget= forms.PasswordInput)

    class Meta:

        model= User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

