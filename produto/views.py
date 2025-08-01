from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto


def index(request):
    produtos = Produto.objects.all
    context = {'produtos':produtos,
               }
    return render(request, 'index.html', context)