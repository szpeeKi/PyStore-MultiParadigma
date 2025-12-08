"""
Módulo Principal: Loja Online Multi-Paradigma

Este arquivo serve como ponto de entrada (Entry Point) da aplicação.
Ele orquestra a interação entre os três paradigmas de programação exigidos:

1. POO: Instanciação de objetos e chamadas de métodos.
2. Funcional: Uso de funções puras para processar dados (Map/Filter/Reduce).
3. Imperativo: Controle de fluxo (While/If) e interação com usuário (Input/Print).
"""

# ----------------------------------------------
# IMPORTAÇÕES — Paradigma Modular
# Importamos classes orientadas a objetos (POO)
# e funções utilitárias que implementam map/filter/reduce
# ----------------------------------------------
from models.Produto import Produto                    # Classe base (Herança / POO)
from models.ProdutoDigital import ProdutoDigital      # Herança
from models.ProdutoFisico import ProdutoFisico        # Herança
from models.Carrinho import Carrinho                  # Objeto que contém outros objetos
from models.Cliente import Cliente                    # Representação orientada a objetos
from models.ItemCarrinho import ItemCarrinho          # Composição: Carrinho -> ItemCarrinho
from utils.analise_dados import calcular_total_carrinho, mapear_resumo_carrinho, filtrar_itens_caros
from utils.persistencia import salvar_estoque, carregar_estoque
# As funções acima usam Map, Filter, Reduce (Programação funcional)

# ----------------------------------------------
# INSTANCIAÇÃO DE OBJETOS — POO (Classes e Objetos)
# Aqui definimos o estado inicial da aplicação criando as entidades.
# ----------------------------------------------

cliente_atual = Cliente("123.456.789-00", 
                        "João da Silva", 
                        "(21) 9999-9999", 
                        "Rua das Flores, 123")

# Tenta carregar do JSON
catalogo_produtos = carregar_estoque()

# Se a lista estiver vazia (primeira execução), cria os produtos padrão
if not catalogo_produtos:
    p1 = ProdutoFisico(1, "Livro de Python", 100.0, 10, 0.5, 20, 15, 3, 20.0)
    p2 = ProdutoDigital(2, "E-book de Python", 50.0, 100, 5, "PDF")
    catalogo_produtos = [p1, p2]

# Helpers para achar o produto na lista (já que agora é uma lista dinâmica)
def buscar_produto_por_id(id_buscado):
    # next() é uma função que itera e retorna o primeiro match
    return next((p for p in catalogo_produtos if p.getCodigo() == id_buscado), None)

# ----------------------------------------------
# CRIAÇÃO DO CARRINHO — OBJETO QUE AGREGA OUTROS OBJETOS
# O Carrinho manterá o estado da compra durante a execução.
# ----------------------------------------------
carrinho = Carrinho()

# ----------------------------------------------
# LOOP PRINCIPAL DO PROGRAMA — PARADIGMA IMPERATIVO
# Controle de fluxo usando while, if/elif/else para gerenciar a execução
# passo a passo baseada nas escolhas do usuário.
# ----------------------------------------------
while True:
    print("\n--- MENU LOJA ---")
    print("1. Adicionar Produto Físico (Livro)")
    print("2. Adicionar Produto Digital (E-book)")
    print("3. Ver Resumo do Carrinho (Map)")
    print("4. Ver Itens Caros > R$ 60 (Filter)")
    print("5. Finalizar Compra/Total (Reduce)")
    print("0. Sair")
    
    opcao = input("Escolha: ")

# ----------------------------------------------
# OPÇÃO 1 — ADICIONAR PRODUTO FÍSICO (POO + Imperativo)
# ----------------------------------------------
    if opcao == "1":
        qtd = int(input("Quantos livros quer? "))
        # Busca o produto ID 1 na lista carregada
        prod = buscar_produto_por_id(1) 
        if prod:
            item = ItemCarrinho(prod, qtd)
            carrinho.adicionar_item(item)
            print("Livro adicionado!")
        else:
            print("Produto não encontrado!")

# ----------------------------------------------
# OPÇÃO 2 — ADICIONAR PRODUTO DIGITAL
# ----------------------------------------------
    elif opcao == "2":
        qtd = int(input("Quantos E-books quer? "))
        # Busca o produto ID 2 na lista carregada
        prod = buscar_produto_por_id(2)
        if prod:
            item = ItemCarrinho(prod, qtd)
            carrinho.adicionar_item(item)
            print("E-book adicionado!")
        else:
            print("Produto não encontrado!")

# ----------------------------------------------
# OPÇÃO 3 — Função MAP (Programação Funcional)
# mapear_resumo_carrinho() aplica uma transformação
# sobre a lista de itens do carrinho, retornando uma nova lista de strings.
# ----------------------------------------------
    elif opcao == "3":
        # Aqui chamamos sua função MAP definida em utils
        resumo = mapear_resumo_carrinho(carrinho)
        for r in resumo:
            print(r)

# ----------------------------------------------
# OPÇÃO 4 — Função FILTER (Programação Funcional)
# filtrar_itens_caros() processa a lista e devolve apenas 
# os itens que satisfazem a condição (Preço > 60).
# ----------------------------------------------
    elif opcao == "4":
        # Aqui chamamos sua função FILTER definida em utils
        caros = filtrar_itens_caros(carrinho, 60.0)
        print(f"Itens acima de R$ 60: {len(caros)}")

# ----------------------------------------------
# OPÇÃO 5 — Função REDUCE (Programação Funcional)
# calcular_total_carrinho() reduz a lista de itens a um único valor total (float).
# ----------------------------------------------
    elif opcao == "5":
        # Aqui chamamos sua função REDUCE definida em utils
        total = calcular_total_carrinho(carrinho)
        print(f"TOTAL DA COMPRA: R$ {total:.2f}")

# ----------------------------------------------
# SAIR — Controle imperativo simples
# ----------------------------------------------
    elif opcao == "0":
        # Salva o estado atual do catálogo (caso tenhamos alterado estoque futuramente)
        salvar_estoque(catalogo_produtos)
        print("Saindo...")
        break

# ----------------------------------------------
# VALIDAÇÃO — Estrutura imperativa
# ----------------------------------------------
    else:
        print("Opção inválida!")