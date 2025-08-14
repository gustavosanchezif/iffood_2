from django.shortcuts import redirect, render

from produto.models import Produto
from .models import Pedido, ProdutoNoPedido

# Create your views here.

def index(request):
    pedido = Pedido.objects.order_by('-id').first()
    produtos = ProdutoNoPedido.objects.filter(pedido=pedido)
    context = {'produtos':produtos,
               }
    return render(request, 'pedidos/index.html', context)


def olhar_produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos':produtos,
               }
    return render(request, 'pedidos/olharprodutos.html', context)


def adicionarNoCarrinho(request,pk):
    pedido = Pedido.objects.order_by('-id').first()
    produto = Produto.objects.get(id=pk)
    
    try:
        prodNoPedido = ProdutoNoPedido.objects.get(produto=produto, pedido=pedido)
    except ProdutoNoPedido.DoesNotExist:
        prodNoPedido = None
    if(prodNoPedido == None):
        prodNoPedido = ProdutoNoPedido(
            produto = produto,
            pedido = pedido,
            quantidade = 1,
        )
        prodNoPedido.save()
    else:
        prodNoPedido.quantidade = prodNoPedido.quantidade+1
        prodNoPedido.save()
    return redirect("/pedido/")


def diminuir(request,pk):
    id_produtoNoPedido = pk
    prodNoPedido = ProdutoNoPedido.objects.get(id=id_produtoNoPedido)
    prodNoPedido.quantidade = prodNoPedido.quantidade - 1
    if prodNoPedido.quantidade == 0:
        prodNoPedido.delete()
    else:
        prodNoPedido.save()
    return redirect("/pedido/")


def aumentar(request,pk):
    id_produtoNoPedido = pk
    prodNoPedido = ProdutoNoPedido.objects.get(id=id_produtoNoPedido)
    prodNoPedido.quantidade = prodNoPedido.quantidade + 1
    prodNoPedido.save()
    return redirect("/pedido/")


def deletar(request,pk):
    id_produtoNoPedido = pk
    prodNoPedido = ProdutoNoPedido.objects.get(id=id_produtoNoPedido)
    prodNoPedido.delete()
    return redirect("/pedido/")



def finalizar(request):
    pedido = Pedido.objects.order_by('-id').first()
    pedido.status = 'solicitado'
    pedido.save()
    pedidoNovo = Pedido(
        status = 'no_carrinho'
    )
    pedidoNovo.save()
    return redirect("/pedido/")

def pedidos_anteriores(request):
    pedidos = Pedido.objects.order_by('-id')[1:]
    context = {
        'pedidos':pedidos,
    }
    return render(request, 'pedidos/pedidos_anteriores.html', context)

def verPedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    produtos = ProdutoNoPedido.objects.filter(pedido=pedido)
    context = {'produtos':produtos,
               }
    return render(request, 'pedidos/verPedido.html', context)