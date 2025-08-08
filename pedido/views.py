from django.shortcuts import redirect, render

from produto.models import Produto
from .models import Pedido, ProdutoNoPedido

# Create your views here.

def index(request):
    id_pedido = 1
    produtos = ProdutoNoPedido.objects.filter(pedido__id=id_pedido)
    context = {'produtos':produtos,
               }
    return render(request, 'pedidos/index.html', context)


def olhar_produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos':produtos,
               }
    return render(request, 'pedidos/olharprodutos.html', context)


def adicionarNoCarrinho(request,pk):
    id_pedido = 1
    produto = Produto.objects.get(id=pk)
    pedido = Pedido.objects.get(id=id_pedido)
    prodNoPedido = ProdutoNoPedido.objects.get(produto=produto, pedido=pedido)
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
