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
# As funções acima usam Map, Filter, Reduce (Programação funcional)

# ----------------------------------------------
# INSTANCIAÇÃO DE OBJETOS — POO (Classes e Objetos)
# Aqui definimos o estado inicial da aplicação criando as entidades.
# ----------------------------------------------

cliente_atual = Cliente("123.456.789-00", 
                        "João da Silva", 
                        "(21) 9999-9999", 
                        "Rua das Flores, 123")

# Produto físico — POO com herança
# Demonstração de Polimorfismo: p1 terá comportamento de frete no cálculo
p1 = ProdutoFisico(codigo=1, 
                   descricao="Livro de Python", 
                   preco=100.0, quantidadeEstoque=10, 
                   peso=0.5, 
                   altura=20, 
                   largura=15, 
                   profundidade=3, 
                   frete=20.0)

# Produto digital — POO com herança
# Demonstração de Polimorfismo: p2 usará o cálculo padrão (sem frete)
p2 = ProdutoDigital(codigo=2, 
                    descricao="E-book de Python", 
                    preco=50.0, 
                    quantidadeEstoque=100, 
                    tamanhoArquivoMB=5, 
                    formatoArquivo="PDF")

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
        item = ItemCarrinho(p1, qtd) # Criação de objeto ItemCarrinho — POO (Composição)
        carrinho.adicionar_item(item) # Chamando método de instância — Encapsulamento
        print("Livro adicionado!")

# ----------------------------------------------
# OPÇÃO 2 — ADICIONAR PRODUTO DIGITAL
# ----------------------------------------------
    elif opcao == "2":
        qtd = int(input("Quantos E-books quer? "))
        item = ItemCarrinho(p2, qtd)
        carrinho.adicionar_item(item)
        print("E-book adicionado!")

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
        break

# ----------------------------------------------
# VALIDAÇÃO — Estrutura imperativa
# ----------------------------------------------
    else:
        print("Opção inválida!")