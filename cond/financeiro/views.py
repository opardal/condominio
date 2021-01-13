from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Despesa


class Despesas(ListView):
    model = Despesa
    context_object_name = 'lista_de_despesas'
    template_name = 'financeiro/despesas.html'


class DespesaDetalhe(DetailView):
    model = Despesa
    template_name = 'financeiro/despesa_detalhe.html'


def index(request):
    context = {}
    return render(request, 'financeiro/index.html', context)

def cadastrar_despesa(request):
    context = {}
    return render(request, 'financeiro/cadastrar_despesa.html', context)

