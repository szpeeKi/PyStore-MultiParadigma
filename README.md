# 🛒 Loja Online: Multi-Paradigma

> Um sistema de e-commerce simulado em Python, demonstrando a aplicação prática de múltiplos paradigmas de programação: **Orientado a Objetos (POO)**, **Funcional** e **Imperativo**, além de **Persistência de Dados**.

---

## 📋 Sobre o Projeto

Este projeto serve como um estudo de caso sobre arquitetura de software. O sistema simula o fluxo de compra de produtos físicos (livros) e digitais (e-books), gerenciando carrinho, cálculo de preços, análise de dados e carregamento dinâmico de inventário via arquivos.

### 🎯 Objetivos Educacionais

O código exemplifica:

| Paradigma/Conceito | Aplicação no Projeto | Localização |
| :--- | :--- | :--- |
| **Orientado a Objetos** | Herança, Polimorfismo, Encapsulamento e Composição. | Pasta `models/` |
| **Funcional** | Map, Filter, Reduce e Funções Puras. | `utils/analise_dados.py` |
| **Persistência** | Leitura e interpretação de arquivos JSON (I/O). | `utils/persistencia.py` |
| **Imperativo** | Controle de fluxo, loops e interação com usuário. | `main.py` |

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
│   │   └── persistencia.py       # Leitura de dados (JSON)
│   │
│   └── main.py                   # --- PONTO DE ENTRADA (Imperativo) ---
│
├── products.json                 # Base de dados dos produtos
└── README.md                     # Documentação