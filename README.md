# Desafio Python: Sistema de Análise de Vendas

**Nível:** Intermediário  
**Tecnologias:** Python (inicialmente sem bibliotecas externas)

## Cenário

Você foi contratado por uma pequena empresa para desenvolver um programa que analise suas vendas mensais.

Utilize os seguintes registros como dados de entrada:

```python
vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "quantidade": 2, "preco": 3500},
    {"produto": "Mouse", "categoria": "Periféricos", "quantidade": 10, "preco": 80},
    {"produto": "Teclado", "categoria": "Periféricos", "quantidade": 5, "preco": 150},
    {"produto": "Monitor", "categoria": "Eletrônicos", "quantidade": 3, "preco": 1200},
    {"produto": "Notebook", "categoria": "Eletrônicos", "quantidade": 1, "preco": 3500},
    {"produto": "Mouse", "categoria": "Periféricos", "quantidade": 15, "preco": 80},
    {"produto": "Headset", "categoria": "Periféricos", "quantidade": 4, "preco": 250},
]
```

## Sua missão

Desenvolva um programa que realize as operações a seguir.

### 1. Faturamento

- Calcular o faturamento total.
- Calcular o faturamento individual de cada produto.
- Calcular a quantidade total de itens vendidos.

### 2. Análise de produtos

- Identificar o produto mais vendido em quantidade.
- Identificar o produto que gerou o maior faturamento.
- Listar os produtos que venderam mais de 5 unidades.

### 3. Análise por categoria

- Calcular o faturamento de cada categoria.
- Identificar a categoria com maior faturamento.
- Calcular a participação percentual de cada categoria no faturamento total.

### 4. Relatório final

Exiba um relatório organizado no terminal. O exemplo abaixo indica a estrutura esperada; os valores devem ser calculados pelo seu programa.

```text
========== RELATÓRIO DE VENDAS ==========

Faturamento total: R$ XX.XXX,XX
Quantidade de itens vendidos: XX

Produto mais vendido: XXXXX
Maior faturamento por produto: XXXXX

========== CATEGORIAS ==========

Eletrônicos: R$ XX.XXX,XX (XX%)
Periféricos: R$ XX.XXX,XX (XX%)
```

## Regras do desafio

- Não utilize bibliotecas externas inicialmente.
- Utilize funções para separar as responsabilidades.
- Evite repetir código.
- Não coloque os cálculos diretamente dentro dos `print()`.
- Utilize dicionários para agrupar os resultados.
- Considere que um mesmo produto pode aparecer em vários registros e some suas vendas antes de identificar os resultados.

## Níveis de dificuldade

### Nível 1 — Fundamentos

Resolva utilizando listas, dicionários, laços de repetição e condicionais.

### Nível 2 — Organização

Transforme cada operação em uma função independente. Organize o código para que cada função tenha uma responsabilidade clara.

### Nível 3 — Pandas

Refaça a análise utilizando Pandas e DataFrames. Compare a solução com a versão desenvolvida sem bibliotecas externas.

### Nível 4 — Visualização

Gere gráficos de faturamento por produto e por categoria utilizando Matplotlib.

## Critérios de conclusão

- [X] Calcular corretamente o faturamento total.
- [X] Identificar os produtos mais vendidos e com maior faturamento.
- [X] Calcular os resultados por categoria e seus percentuais.
- [X] Exibir um relatório legível no terminal.
- [X] Separar as responsabilidades em funções (a partir do nível 2).
