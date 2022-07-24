from django.contrib import admin
from Inmuebles.models import Venta, Alquiler, Avatar

# Register your models here.

admin.site.register(Venta)
admin.site.register(Alquiler)
admin.site.register(Avatar)