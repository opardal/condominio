from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_despesa', views.cadastrar_despesa, name='cadastrar_despesa'),
]