from django.urls import path
from Inmuebles import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('venta', views.venta, name="Venta"),
    path('alquiler', views.alquiler, name="Alquiler"),
    path('about', views.about, name="About"),
    path('busqueda', views.busqueda),

    path('venta/list', views.VentaList.as_view(), name = 'List'),
    path(r'^(?P<pk>\d+)$', views.VentaDetalle.as_view(), name = 'Detail'),
    path(r'^nuevo$', views.VentaCreacion.as_view(), name = 'New'),
    path(r'^editar/(?P<pk>\d+)$', views.VentaUpdate.as_view(), name ='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.VentaDelete.as_view(), name = 'Delete'),

    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='Inmuebles/logout.html'), name= 'Logout'),
    path('editarPerfil', views.editarPerfil, name= "EditarPerfil"),


]