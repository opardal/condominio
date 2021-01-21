from django import forms
from .models import Competencia, Despesa


class CompetenciaForm(forms.Form):
    competencia = forms.IntegerField(widget=forms.Select(attrs = {'onchange' : "this.form.submit()"},
                                                         choices=[(c.id, c) for c in Competencia.objects.all()]))


class DespesaForm(forms.ModelForm):

    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'competencia']

    def __init__(self, *args, **kwargs):
        super(DespesaForm, self).__init__(*args, **kwargs)
        if kwargs['initial']['ocultar_campo']:
            self.fields['competencia'].widget = forms.HiddenInput()
