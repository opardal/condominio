from django.urls import path

from . import views

app_name = 'financeiro'
urlpatterns = [
    path('', views.FinanceiroIndex.as_view(), name='index'),
    path('despesas/', views.Despesas.as_view(), name='despesas'),
    path('despesas/<int:pk>/', views.DespesaDetalhe.as_view(), name='despesa-detail'),
    path('despesas/add/', views.DespesaCreate.as_view(), name='despesa-add'),
    path('<competencia>/despesas/', views.Despesas.as_view(), name='despesas-comp'),
    path('<competencia>/despesas/<int:pk>/', views.DespesaDetalhe.as_view(), name='despesa-detail-comp'),
    path('<competencia>/despesas/add/', views.DespesaCreate.as_view(), name='despesa-add-comp'),
    path('despesas/<int:pk>/update/', views.DespesaUpdate.as_view(), name='despesa-update'),
    path('despesas/<int:pk>/delete/', views.DespesaDelete.as_view(), name='despesa-delete'),
    path('boletos/', views.Boletos.as_view(), name='boletos'),
]
