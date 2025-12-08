#Título: Loja Online: Multi-Paradigma
## Descrição do projeto 
O que faz o app: Compra de Produto Físico (Livro) e Produto Digital (E-book)
Como foi construído: na plataforma GitHub que é uma plataforma de desenvolvimento baseada na nuvem que usa o sistema de controle de versão Git para hospedar, gerenciar e colaborar em projetos de software, funcionando como um "hub" para desenvolvedores compartilharem código, rastrearem alterações e gerenciarem tarefas. Projeto desenvolvido em Python, demonstrando princípios de multiparadigma, estruturado, funcional e Programação Orientada a Objetos (POO).
Estrutura do Projeto
/files/
 ├── models
	├── _pycache_
	 Carrinho.py
	 Cliente.py
	 ItemCarrinho.py
	 Produto.py
 ProdutoDigital.py
 ProdutoFisico.py
  ├── utils
	├── _pycache_
	 analise_dadoscpython-311.pyc
         analise_dados.py
   main.py

├── products.json
 └── README.md   ← este arquivo
  
Objetivo do Sistema
O projeto simula:
•	Cadastro e carregamento de produtos a partir de arquivo JSON
•	Carrinho de compras com inclusão/remoção de itens
•	Classes que utilizam herança, polimorfismo, abstração e encapsulamento
•	Análise de dados simples com módulo separado (analise_dados.py)
--- MENU LOJA ---
1. Adicionar Produto Físico (Livro)
2. Adicionar Produto Digital (E-book)
3. Ver Resumo do Carrinho (Map)
4. Ver Itens Caros > R$ 60 (Filter)
5. Finalizar Compra/Total (Reduce)
0. Sair

Tecnologias Utilizadas
Python 3.10+
JSON
Conceitos de POO, funcional, imperativo

Como Executar o Projeto
1️ - Certifique-se de ter Python instalado
2 - Execute o programa principal
3 - Para rodar as análises de dados

Função de Carregamento de Produtos
O main.py utiliza:
from utils import carregar_produtos
produtos = carregar_produtos("products.json")

Essa função:
Lê o JSON
Identifica o tipo (digital/físico)
Instancia a classe correta

Comentários Paradigmáticos Inseridos no Código
Todos os arquivos .py possuem comentários como:
# --- EXEMPLO DE POLIMORFISMO ---
# Subclasses implementam calcular_preco_final() de formas diferentes

# --- ENCAPSULAMENTO ---
# Uso de propriedades para proteger atributos internos

# --- HERANÇA ---
# ProdutoDigital e ProdutoFisico herdam da classe Produto

# --- COMPOSIÇÃO ---
# ItemCarrinho contém um Produto dentro dele

Diagrama UML
O projeto inclui as classes:
•	Produto (abstrata)
•	ProdutoFisico
•	ProdutoDigital
•	Cliente
•	Carrinho
•	ItemCarrinho

 
Descrição textual do UML
Produto (abstract)
 ├── + nome: str
 ├── + preco: float
 ├── + calcular_preco_final(): float (abstract)
 └── + __str__()

ProdutoFisico : Produto
 ├── + peso: float
 └── + calcular_preco_final()

ProdutoDigital : Produto
 ├── + tamanho_mb: int
 └── + calcular_preco_final()

Cliente
 ├── + nome: str
 └── + email: str

ItemCarrinho
 ├── + produto: Produto
 ├── + quantidade: int
 └── + subtotal(): float

Carrinho
 ├── + itens: list[ItemCarrinho]
 ├── + adicionar_item()
 ├── + remover_item()
 └── + total(): float
