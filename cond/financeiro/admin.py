from django.contrib import admin

# Register your models here.

from .models import Despesa, Boleto, Competencia

admin.site.register(Despesa)
admin.site.register(Boleto)
admin.site.register(Competencia)