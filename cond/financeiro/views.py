from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'financeiro/index.html', context)

def cadastrar_despesa(request):
    context = {}
    return render(request, 'financeiro/cadastrar_despesa.html', context)
