from django.contrib import admin

from .models import Pedido, ProdutoNoPedido

# Register your models here.
admin.site.register(Pedido)
admin.site.register(ProdutoNoPedido)
