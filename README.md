# 🛒 Loja Online: Multi-Paradigma

> Um sistema de e-commerce simulado em Python, demonstrando a aplicação prática de múltiplos paradigmas de programação: Orientado a Objetos (POO), Funcional e Imperativo.

## 📋 Sobre o Projeto

Este projeto tem como objetivo principal servir como um estudo de caso sobre arquitetura de software e aplicação de conceitos avançados de programação. O sistema simula o fluxo de compra de produtos físicos (livros) e digitais (e-books), gerenciando carrinho, cálculo de preços e análise de dados.

### 🎯 Objetivos Educacionais
O código foi estruturado para exemplificar explicitamente:
* **POO:** Herança, Polimorfismo, Abstração, Encapsulamento e Composição.
* **Funcional:** Uso de funções de alta ordem como `map`, `filter` e `reduce` para manipulação de dados.
* **Imperativo:** Controle de fluxo de execução e estados.
* **Persistência de Dados:** Leitura e interpretação de arquivos JSON.

---

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Formato de Dados:** JSON
* **Bibliotecas:** Padrão do Python (`json`, `functools`, etc.)

---

## 📂 Estrutura do Projeto

```text
/
├── files/
│   ├── models/
│   │   ├── Carrinho.py       # Gerencia a coleção de itens
│   │   ├── Cliente.py        # Dados do usuário
│   │   ├── ItemCarrinho.py   # Composição (Produto + Quantidade)
│   │   ├── Produto.py        # Classe Abstrata
│   │   ├── ProdutoDigital.py # Herança (E-book)
│   │   └── ProdutoFisico.py  # Herança (Livro Físico)
│   ├── utils/
│   │   └── analise_dados.py  # Módulo de análise estatística
│   └── main.py               # Ponto de entrada (Menu e Execução)
├── products.json             # Base de dados dos produtos
└── README.md                 # Documentação do projeto