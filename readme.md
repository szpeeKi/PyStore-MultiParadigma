## 🎓 Projeto Acadêmico

Este projeto foi desenvolvido como parte de um trabalho acadêmico para a faculdade, com o objetivo de demonstrar a aplicação prática de diferentes paradigmas de programação em um sistema de e-commerce.

# PyStore Multi-Paradigma 🛒

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Concluído-green)

## 💻 Sobre o Projeto

Este projeto é uma simulação de um sistema de e-commerce desenvolvida em **Python**. O objetivo principal não é apenas criar uma loja, mas sim demonstrar a aplicação prática e simultânea de três paradigmas de programação diferentes em um único sistema:

1.  **Orientação a Objetos (POO):** Para modelagem das entidades (Produtos, Clientes, Carrinho).
2.  **Programação Funcional:** Para análise e processamento de dados sem efeitos colaterais (Map, Filter, Reduce).
3.  **Programação Imperativa:** Para o controle de fluxo e interação com o usuário via terminal.

## ⚙️ Funcionalidades

- [x] **Catálogo Híbrido:** Suporte para Produtos Físicos (com frete) e Digitais (arquivos).
- [x] **Carrinho de Compras:** Adição e cálculo de totais.
- [x] **Persistência de Dados:** Salvamento e carregamento automático de estoque via JSON.
- [x] **Análise de Dados (Funcional):**
    - Resumo de itens (Map).
    - Filtragem de itens de alto valor (Filter).
    - Cálculo total consolidado (Reduce).

## 📚 Conceitos Aplicados

### 1. Orientação a Objetos
O sistema utiliza conceitos avançados de POO na pasta `models`:
* **Herança:** `ProdutoFisico` e `ProdutoDigital` herdam de `Produto`.
* **Polimorfismo:** O método `calcular_valor_final()` se comporta de maneira diferente dependendo se o produto tem frete ou não.
* **Encapsulamento:** Uso de atributos protegidos (ex: `_preco`) e Getters/Setters.
* **Composição:** O `Carrinho` é composto por vários objetos `ItemCarrinho`.

### 2. Programação Funcional
Localizada em `utils/analise_dados.py`, utilizamos funções puras e lambda para tratar listas:
* **Map:** Transforma objetos complexos em dicionários simples para relatórios.
* **Filter:** Isola produtos acima de um determinado valor (ex: > R$ 60,00).
* **Reduce:** Acumula o valor total de todos os itens do carrinho em uma única soma.

## 📂 Estrutura do Projeto

A organização dos arquivos deve seguir este padrão para que os *imports* do Python funcionem:

```bash
/
├── main.py                  # Arquivo principal (Entry Point)
├── products.json            # Banco de dados local (gerado automaticamente)
│
├── models/                  # Camada de Domínio (Classes POO)
│   ├── Carrinho.py
│   ├── Cliente.py
│   ├── ItemCarrinho.py
│   ├── Produto.py
│   ├── ProdutoDigital.py
│   └── ProdutoFisico.py
│
└── utils/                   # Utilitários (Funcional e Persistência)
    ├── analise_dados.py     # Lógica Funcional (Map/Filter/Reduce)
    └── persistencia.py      # Leitura e Escrita de JSON

## 🚀 Como Executar

### Pré-requisitos
É necessário ter o **Python 3.x** instalado.

### Passo a passo

1. Clone o repositório:

```bash
git clone https://github.com/szpeeKi/PyStore-MultiParadigma.git
```

2. Acesse a pasta do projeto:

```bash
cd PyStore-MultiParadigma
```

3. Execute o arquivo principal:

```bash
python main.py
```

## 📝 Exemplo de Uso (Terminal)

--- MENU LOJA ---
1. Adicionar Produto Físico (Livro)
2. Adicionar Produto Digital (E-book)
3. Ver Resumo do Carrinho (Map)
4. Ver Itens Caros > R$ 60 (Filter)
5. Finalizar Compra/Total (Reduce)
0. Sair
Escolha:

✒️ Autor
Desenvolvido por szpeeKi.