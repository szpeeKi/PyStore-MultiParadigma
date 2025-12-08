# 🛒 Loja Online: Multi-Paradigma

> Um sistema de e-commerce simulado em Python, demonstrando a aplicação prática de múltiplos paradigmas de programação: **Orientado a Objetos (POO)**, **Funcional** e **Imperativo**, com persistência de dados em JSON.

---

## 📋 Sobre o Projeto

Este projeto serve como um estudo de caso sobre arquitetura de software. O sistema simula o fluxo de compra de produtos físicos (livros) e digitais (e-books), gerenciando carrinho, cálculo de preços, análise de dados e carregamento dinâmico de inventário via arquivos.

### 🎯 Objetivos Educacionais

O código exemplifica explicitamente:

| Paradigma/Conceito | Aplicação no Projeto | Localização |
| :--- | :--- | :--- |
| **Orientado a Objetos** | Herança, Polimorfismo, Encapsulamento e Composição. | Pasta `files/models/` |
| **Funcional** | Map, Filter, Reduce e Funções Puras. | `files/utils/analise_dados.py` |
| **Persistência** | Leitura e interpretação de arquivos JSON. | `files/utils/persistencia.py` |
| **Imperativo** | Controle de fluxo e interação com usuário. | `files/main.py` |

---

## 📂 Estrutura do Projeto

A organização segue o princípio de separação de responsabilidades:

```text
/
├── files/
│   ├── models/                   # --- CAMADA DE DOMÍNIO (POO) ---
│   │   ├── Carrinho.py           # Agregador de itens
│   │   ├── Cliente.py            # Dados encapsulados
│   │   ├── ItemCarrinho.py       # Wrapper (Produto + Quantidade)
│   │   ├── Produto.py            # Classe Abstrata
│   │   ├── ProdutoDigital.py     # Subclasse (E-book)
│   │   └── ProdutoFisico.py      # Subclasse (Livro Físico)
│   │
│   ├── utils/                    # --- CAMADA DE UTILITÁRIOS ---
│   │   ├── analise_dados.py      # Funções de Map/Filter/Reduce
│   │   └── persistencia.py       # Carregamento de dados (JSON)
│   │
│   └── main.py                   # --- PONTO DE ENTRADA (Imperativo) ---
│
├── products.json                 # Base de dados dos produtos
└── README.md                     # Documentação

🧩 Diagrama de Classes (UML)
O sistema utiliza herança para especializar os produtos e composição para montar o carrinho.

Snippet de código

classDiagram
    class Produto {
        <<Abstract>>
        +calcular_valor_final()*
    }
    class ProdutoFisico {
        +float frete
        +calcular_valor_final()
    }
    class ProdutoDigital {
        +int tamanho_mb
        +calcular_valor_final()
    }
    class Carrinho {
        +list itens
        +adicionar_item()
    }

    Produto <|-- ProdutoFisico : Herança
    Produto <|-- ProdutoDigital : Herança
    Carrinho *-- ItemCarrinho : Composição
    ItemCarrinho o-- Produto : Agregação
🚀 Funcionalidades Detalhadas
1. Carregamento de Dados (persistencia.py)
O sistema lê o arquivo products.json, identifica o tipo de produto (Físico ou Digital) e instancia a classe correta automaticamente (Padrão Factory).

2. Análise de Dados (analise_dados.py)
Utiliza Programação Funcional para gerar relatórios:

MAP: Cria resumos simplificados do carrinho.

FILTER: Filtra itens de alto valor.

REDUCE: Calcula o total financeiro da compra.

3. Regras de Negócio (POO)
Polimorfismo: O método calcular_valor_final soma o frete apenas se o produto for físico.

Encapsulamento: Atributos protegidos acessados via Getters e Setters.

🛠 Como Executar o Projeto
Para rodar o projeto corretamente, é necessário executar o script principal a partir da pasta raiz, para que ele encontre o arquivo products.json.

Passo a Passo
Certifique-se de ter o Python 3.10+ instalado.

Abra o terminal na pasta raiz do projeto (onde está o arquivo README.md e products.json).

Execute o comando:

Bash

python files/main.py
(Caso esteja no Linux ou Mac, utilize python3 files/main.py)