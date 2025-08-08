from django.db import models

from produto.models import Produto

class Pedido(models.Model):
    STATUS_CHOICES = [
            ('no_carrinho', 'No carrinho'),
            ('solicitado', 'Solicitado'),
            ('em_producao', 'Em produção'),
            ('entregue', 'Entregue'),
        ]

    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='no_carrinho',
        )

    def __str__(self):
        return str(self.id) + " - " +self.status

class ProdutoNoPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.produto.name + " - " +str(self.quantidade)