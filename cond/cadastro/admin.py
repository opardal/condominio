from django.contrib import admin

# Register your models here.

from .models import Condominio, Economia

admin.site.register(Condominio)
admin.site.register(Economia)