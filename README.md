# SAT Solvers

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-orange.svg)
![Algorithms](https://img.shields.io/badge/Algorithms-SAT%20Solving-purple.svg)

CLI educacional para estudo e comparação de algoritmos clássicos de resolução do Problema da Satisfatibilidade Booleana (SAT).

## Algoritmos Implementados

| Algoritmo    | Status |
| ------------ | ------ |
| Brute Force  | ✅      |
| Davis-Putnam | ✅      |
| DPLL         | ✅      |
| CDCL         | 🚧     |

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/sat-solvers.git
cd sat-solvers
```

Crie e ative um ambiente virtual:

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Formato CNF (DIMACS)

O framework utiliza arquivos no formato DIMACS.

Exemplo:

```text
p cnf 3 3

1 2 0
-1 3 0
-2 3 0
```

Representa:

```text
(A ∨ B)
∧
(¬A ∨ C)
∧
(¬B ∨ C)
```

## Utilização

### Resolver uma instância SAT

Sintaxe:

```bash
python main.py solve <solver> <arquivo.cnf>
```

Exemplos:

```bash
python main.py solve brute_force examples/sample.cnf
```

```bash
python main.py solve davis_putnam examples/sample.cnf
```

```bash
python main.py solve dpll examples/sample.cnf
```

```bash
python main.py solve cdcl examples/sample.cnf
```

Saída:

```text
Result: SAT
```

ou

```text
Result: UNSAT
```

## Benchmark

Executar benchmark de um algoritmo específico:

```bash
python main.py benchmark brute_force
```

```bash
python main.py benchmark davis_putnam
```

```bash
python main.py benchmark dpll
```

```bash
python main.py benchmark cdcl
```

Executar benchmark de todos os algoritmos:

```bash
python main.py benchmark all
```

Exemplo de saída:

```text
============================================================
BENCHMARK DPLL
============================================================

Variables: 20
Result: SAT
Execution Time: 0.0012s
```

## Estrutura do Projeto

```text
.
├── brute_force/
│   └── solver.py
│
├── davis_putnam/
│   └── solver.py
│
├── DPLL/
│   └── solver.py
│
├── CDCL/
│   └── solver.py
│
├── stats/
├── cnf.py
├── helpers.py
├── type_alias.py
├── main.py
└── README.md
```

## Objetivo

Este projeto tem como objetivo demonstrar a evolução histórica dos algoritmos SAT:

```text
Brute Force
    ↓
Davis-Putnam
    ↓
DPLL
    ↓
CDCL
```

permitindo comparar desempenho, estratégias de busca e técnicas de poda utilizadas por cada abordagem.

## Referências

* Martin Davis & Hilary Putnam (1960)
* Davis, Logemann & Loveland (1962)
* Marques-Silva & Sakallah (1999)
* Handbook of Satisfiability
