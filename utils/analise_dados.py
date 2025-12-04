from functools import reduce

def calcular_total_carrinho(carrinho):
    return reduce(lambda total, item: total + item.calcular_valor_total(), carrinho.listar_itens(), 0)

def mapear_resumo_carrinho(carrinho):
    return list(map(lambda item: {
        'codigo': item.getProduto().getCodigo(),
        'descricao': item.getProduto().getDescricao(),
        'quantidade': item.getQuantidade(),
        'valor_unitario': item.getProduto().getPreco(),
        'valor_total': item.calcular_valor_total()
    }, carrinho.listar_itens()))

def filtrar_itens_caros(carrinho, limite):
    return list(filter(lambda item: item.calcular_valor_total() > limite, carrinho.listar_itens()))