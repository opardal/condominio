from django.urls import path

from . import views

app_name = 'financeiro'
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_despesa', views.cadastrar_despesa, name='cadastrar_despesa'),
    path('despesas/', views.Despesas.as_view()),
    path('despesas/<int:pk>/', views.DespesaDetalhe.as_view(), name='despesa_detalhe'),
]
