from django.shortcuts import render
from Inmuebles.models import Venta, Alquiler, Avatar
from Inmuebles.forms import VentaForm, AlquilerForm, UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# @login_required
def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)
        
    try: 
        
        return render(request, "Inmuebles/inicio.html", {"url":avatares[0].imagen.url})
    
    except IndexError:

        return render(request, "Inmuebles/inicio.html")

@login_required
def venta(request):

    if request.method == "POST":

        form = VentaForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            venta = Venta (ubicacion=info['ubicacion'], direccion=info['direccion'], precio=info['precio'], habitaciones=info['habitaciones'])

            venta.save()
            avatares = Avatar.objects.filter(user=request.user.id)

            return render(request, "Inmuebles/inicio.html", {"url":avatares[0].imagen.url})

    else:

        form = VentaForm()
        avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "Inmuebles/venta.html", {"form":form , "url":avatares[0].imagen.url})

@login_required
def alquiler(request):

    if request.method == "POST":

        form = AlquilerForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            alquiler = Alquiler (ubicacion=info['ubicacion'], direccion=info['direccion'], precio=info['precio'], habitaciones=info['habitaciones'])

            alquiler.save()

            return render(request, "Inmuebles/inicio.html")

    else:

        form = AlquilerForm()
        avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "Inmuebles/alquiler.html", {"form":form , "url":avatares[0].imagen.url})

def about(request):

    return render(request, "Inmuebles/about.html")



def busqueda(request):

    if request.GET['ubicacion']:

        ubicacion= request.GET['ubicacion']
        ventas= Venta.objects.filter(ubicacion__icontains=ubicacion)

        return render(request, "Inmuebles/inicio.html", {"ventas":ventas, "ubicacion":ubicacion})
    
    else:

        respuesta = "No enviaste datos"

    return render(request, "Inmuebles/inicio.html", {"respuesta":respuesta})


    

class VentaList(LoginRequiredMixin, ListView):

    model = Venta
    template_name = "Inmuebles/venta_list.html"

class VentaDetalle(DetailView):

    model = Venta
    template_name = "Inmuebles/venta_detalle.html"

class VentaCreacion(CreateView):

    model = Venta
    success_url = "/Inmuebles/venta/list"
    fields = ['ubicacion', 'direccion', 'precio', 'habitaciones']

class VentaUpdate(UpdateView):

    model = Venta
    success_url = "/Inmuebles/venta/list"
    fields = ['ubicacion', 'direccion', 'precio', 'habitaciones']

class VentaDelete(DeleteView):

    model = Venta
    success_url = "/Inmuebles/venta/list"

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)

                return render(request, "Inmuebles/inicio.html", {"url":avatares[0].imagen.url ,"mensaje": f"Bienvenido {usuario}"})
            
            else: 

                return render(request, "Inmuebles/inicio.html", {"mensaje": "Error, datos incorrectos"})

        else:

                return render(request, "Inmuebles/inicio.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Inmuebles/login.html", {'form':form})

def register(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, "Inmuebles/inicio.html", {"mensaje": "Usuario creado"})

    else:

        form = UserRegisterForm()

    return render(request, "Inmuebles/registro.html", {"form": form})

@login_required
def editarPerfil(request):

    usuario= request.user

    if request.method == "POST":
        form= UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()
            avatares = Avatar.objects.filter(user=request.user.id)

            return render(request, "Inmuebles/inicio.html", {"url":avatares[0].imagen.url})

    else:

        form= UserEditForm(initial={'email':usuario.email})
        avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "Inmuebles/editarPerfil.html", {"form":form, "usuario":usuario , "url":avatares[0].imagen.url})

