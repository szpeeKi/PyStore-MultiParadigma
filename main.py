from models.Produto import Produto
from models.ProdutoDigital import ProdutoDigital
from models.ProdutoFisico import ProdutoFisico
from models.Carrinho import Carrinho
from models.ItemCarrinho import ItemCarrinho
from utils.analise_dados import calcular_total_carrinho, mapear_resumo_carrinho, filtrar_itens_caros

p1 = ProdutoFisico(codigo=1, descricao="Livro de Python", preco=100.0, quantidadeEstoque=10, peso=0.5, altura=20, largura=15, profundidade=3, frete=20.0)
p2 = ProdutoDigital(codigo=2, descricao="E-book de Python", preco=50.0, quantidadeEstoque=100, tamanhoArquivoMB=5, formatoArquivo="PDF")

# ... (seus imports e criação de p1/p2 aqui em cima)

# Criando o carrinho
carrinho = Carrinho()

while True:
    print("\n--- MENU LOJA ---")
    print("1. Adicionar Produto Físico (Livro)")
    print("2. Adicionar Produto Digital (E-book)")
    print("3. Ver Resumo do Carrinho (Map)")
    print("4. Ver Itens Caros > R$ 60 (Filter)")
    print("5. Finalizar Compra/Total (Reduce)")
    print("0. Sair")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        qtd = int(input("Quantos livros quer? "))
        item = ItemCarrinho(p1, qtd) # Cria o item
        carrinho.adicionar_item(item) # Põe no carrinho
        print("Livro adicionado!")

    elif opcao == "2":
        qtd = int(input("Quantos E-books quer? "))
        item = ItemCarrinho(p2, qtd)
        carrinho.adicionar_item(item)
        print("E-book adicionado!")

    elif opcao == "3":
        # Aqui chamamos sua função MAP
        resumo = mapear_resumo_carrinho(carrinho)
        for r in resumo:
            print(r)

    elif opcao == "4":
        # Aqui chamamos sua função FILTER
        caros = filtrar_itens_caros(carrinho, 60.0)
        print(f"Itens acima de R$ 60: {len(caros)}")

    elif opcao == "5":
        # Aqui chamamos sua função REDUCE
        total = calcular_total_carrinho(carrinho)
        print(f"TOTAL DA COMPRA: R$ {total:.2f}")

    elif opcao == "0":
        break
        
    else:
        print("Opção inválida!")