import json
from models.ProdutoFisico import ProdutoFisico
from models.ProdutoDigital import ProdutoDigital

def salvar_estoque(lista_produtos, nome_arquivo="products.json"):
    try:
        # PARADIGMA FUNCIONAL: map()
        # Transforma lista de Objetos em lista de Dicionários
        lista_dicts = list(map(lambda p: p.to_dict(), lista_produtos))
        
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(lista_dicts, arquivo, indent=4, ensure_ascii=False)
        print(f"Dados salvos em '{nome_arquivo}'!")
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def carregar_estoque(nome_arquivo="products.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        
        produtos = []
        for item in dados:
            # Reconstrói os objetos baseado no campo 'tipo'
            if item["tipo"] == "Físico":
                novo = ProdutoFisico(
                    item["codigo"], item["descricao"], item["preco"], 
                    item["quantidadeEstoque"], item["peso"], item["altura"], 
                    item["largura"], item["profundidade"], item["frete"]
                )
            elif item["tipo"] == "Digital":
                novo = ProdutoDigital(
                    item["codigo"], item["descricao"], item["preco"], 
                    item["quantidadeEstoque"], item["tamanhoArquivoMB"], 
                    item["formatoArquivo"]
                )
            produtos.append(novo)
        return produtos
    except FileNotFoundError:
        return [] # Retorna lista vazia se não existir arquivo