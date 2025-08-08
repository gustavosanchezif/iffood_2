from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Produto


def index(request):
    produtos = Produto.objects.all
    context = {'produtos':produtos,
               }
    return render(request, 'produto/index.html', context)

def adicionar(request):
    nome = request.POST["nome"]
    valor = request.POST["valor"]
    produto_novo = Produto(
        name = nome,
        valor = valor
    )

    produto_novo.save()
    return redirect("/produto/")

def deletar(request, pk):
    produto = Produto.objects.get(id=pk)
    produto.delete()
    return redirect("/produto/")


def editar_form(request, pk):
    produto = Produto.objects.get(id=pk)
    context = {
        'produto': produto
    }
    return render(request, 'produto/editar.html', context)

def editar(request, pk):
    produto = Produto.objects.get(id=pk)
    produto.name = request.POST["nome"]
    produto.valor = request.POST["valor"]
    produto.save()
    return redirect("/produto/")
