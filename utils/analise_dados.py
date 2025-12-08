"""
Módulo de Análise de Dados - Paradigma Funcional.

Este arquivo concentra as funções puras do sistema, que não alteram o estado 
dos objetos, mas sim transformam dados de entrada em novas saídas.

Conceitos aplicados:
1. Funções de Alta Ordem (Map, Filter, Reduce).
2. Funções Lambda (Anônimas).
3. Imutabilidade (gera novas listas em vez de alterar a existente).
"""

# Funções utilitárias
from functools import reduce

def calcular_total_carrinho(carrinho): 
    """
    Calcula o valor total de todos os itens no carrinho.
    
    Paradigma Funcional: REDUCE
    - Reduz uma lista de muitos itens a um único valor (float).
    - Usa uma função lambda acumuladora: 'total' acumula a soma, 'item' é o objeto atual.
    """
    # reduce(funcao, lista, valor_inicial)
    return reduce(
        lambda total, item: total + item.calcular_valor_total(), 
        carrinho.listar_itens(), 
        0
    ) 

def mapear_resumo_carrinho(carrinho): 
    """
    Aplica uma transformação sobre a lista de itens do carrinho.

    Paradigma Funcional: MAP
    - Transforma a lista de objetos 'ItemCarrinho' em uma lista de Dicionários.
    - Útil para criar visualizações ou JSONs sem expor o objeto original.

    Returns:
        list: Uma lista com os dicionários transformados contendo:
              - 'codigo', 'descricao', 'quantidade', 'valor_unitario', 'valor_total'
    """
    return list(map(lambda item: { 
        'codigo': item.getProduto().getCodigo(), 
        'descricao': item.getProduto().getDescricao(), 
        'quantidade': item.getQuantidade(), 
        'valor_unitario': item.getProduto().getPreco(), 
        'valor_total': item.calcular_valor_total() 
    }, carrinho.listar_itens())) 
 
def filtrar_itens_caros(carrinho, limite):
    """ 
    Filtra os itens do carrinho com valor total maior que o limite.
    
    Paradigma Funcional: FILTER
    - Cria uma nova lista contendo APENAS os elementos que retornam True na função lambda.

    Parameters:
        carrinho (Carrinho): O carrinho com os itens a serem filtrados
        limite (float): O valor limite para a filtragem

    Returns:
        list: Uma lista com os itens do carrinho cujo valor total é maior que o limite
    """
    return list(filter(
        lambda item: item.calcular_valor_total() > limite, 
        carrinho.listar_itens()
    ))