from django import forms
from .models import Competencia


class CompetenciaForm(forms.Form):
    competencia = forms.IntegerField(widget=forms.Select(attrs = {'onchange' : "this.form.submit()"},
                                                         choices=[(c.id, c) for c in Competencia.objects.all()]))