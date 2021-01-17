from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .models import Despesa, Boleto, Competencia
from .forms import CompetenciaForm



class Despesas(ListView):
    model = Despesa
    context_object_name = 'lista_de_despesas'
    template_name = 'financeiro/despesas.html'


class DespesaDetalhe(DetailView):
    model = Despesa
    template_name = 'financeiro/despesa_detail.html'


class DespesaCreate(CreateView):
    model = Despesa
    fields = ['nome', 'valor', 'competencia']


class DespesaUpdate(UpdateView):
    model = Despesa
    fields = ['nome', 'valor', 'competencia']


class DespesaDelete(DeleteView):
    model = Despesa
    success_url = reverse_lazy('financeiro:despesas')


class Boletos(ListView):
    model = Boleto
    context_object_name = 'lista_de_boletos'
    template_name = 'financeiro/boletos.html'


class FinanceiroIndex(TemplateView):
    template_name = 'financeiro/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competencia_selecionada'] = 0
        #context['form'] = CompetenciaForm(initial={'competencia':2})
        return context
    
    def get (self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = CompetenciaForm(initial={'competencia':context['competencia_selecionada']})
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['competencia_selecionada'] = request.POST['competencia']
        context['form'] = CompetenciaForm(initial={'competencia':context['competencia_selecionada']})
        return render(request, self.template_name, context)

