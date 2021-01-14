from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .models import Despesa



class Despesas(ListView):
    model = Despesa
    context_object_name = 'lista_de_despesas'
    template_name = 'financeiro/despesas.html'


class DespesaDetalhe(DetailView):
    model = Despesa
    template_name = 'financeiro/despesa_detail.html'


class DespesaCreate(CreateView):
    model = Despesa
    fields = ['nome', 'valor']


class DespesaUpdate(UpdateView):
    model = Despesa
    fields = ['nome', 'valor']


class DespesaDelete(DeleteView):
    model = Despesa
    success_url = reverse_lazy('financeiro:despesas')


def index(request):
    context = {}
    return render(request, 'financeiro/index.html', context)
