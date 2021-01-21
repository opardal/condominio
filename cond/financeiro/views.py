from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Despesa, Boleto, Competencia
from .forms import CompetenciaForm, DespesaForm


class Despesas(ListView):
    context_object_name = 'lista_de_despesas'
    template_name = 'financeiro/despesas.html'
    
    def get_queryset(self):

        try:
            competencia = self.kwargs['competencia']
            ano = competencia[:4]
            mes = competencia[4:]
            comp = Competencia.objects.get(ano=ano, mes=mes)
            query_set = Despesa.objects.filter(competencia=comp)
        except KeyError:
            query_set = Despesa.objects.all()
        return query_set

    def get_context_data(self):
        context = super().get_context_data()
        try:
            context['competencia'] = self.kwargs['competencia']
            context['exibir_por_competencia'] = True
        except KeyError:
            context['exibir_por_competencia'] = False
        return context


class DespesaDetalhe(DetailView):
    model = Despesa
    template_name = 'financeiro/despesa_detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data()

        try:
            context['competencia'] = self.kwargs['competencia']
            context['exibir_por_competencia'] = True
        except KeyError:
            context['exibir_por_competencia'] = False

        return context


class DespesaCreate(CreateView):
    form_class = DespesaForm
    template_name = 'financeiro/despesa_form.html'

    def get_success_url(self):
        try:
            success_url = reverse('financeiro:despesas-comp', kwargs={'competencia': self.kwargs['competencia']})
        except KeyError:
            success_url = reverse('financeiro:despesas')
        return success_url

    def get_initial(self):

        try:
            competencia = self.kwargs['competencia']
            ano = competencia[:4]
            mes = competencia[4:] 
            comp = Competencia.objects.get(ano=ano, mes=mes)
            initial = {'competencia': comp.id, 'is_comp': True}
        except KeyError:
            comp = Competencia.objects.last()
            initial = {'competencia': comp.id, 'is_comp': False}
        return initial

    def get_context_data(self, **kwargs):

        context = super().get_context_data()

        try:
            context['competencia'] = self.kwargs['competencia']
            context['exibir_por_competencia'] = True
        except KeyError:
            context['exibir_por_competencia'] = False
        return context


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
        context['competencia_selecionada'] = 1
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = CompetenciaForm(initial={'competencia':context['competencia_selecionada']})
        context['competencia_str'] = Competencia.objects.get(id=context['competencia_selecionada'])
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['competencia_selecionada'] = request.POST['competencia']
        context['form'] = CompetenciaForm(initial={'competencia':context['competencia_selecionada']})
        context['competencia_str'] = Competencia.objects.get(id=context['competencia_selecionada'])
        return render(request, self.template_name, context)
