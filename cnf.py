"""
cnf.py
"""

import random

from collections import Counter
from collections.abc import Callable, Iterable

from helpers import timed
from type_alias import CNF, Literal, Clause, Variable

# ==========================================================
# Random CNF Generator
# ==========================================================

def random_cnf(
    num_vars: int,
    num_clauses: int,
    clause_size: int = 3,
) -> CNF:

    cnf: CNF = []

    for _ in range(num_clauses):

        clause: set[Literal] = set()
        while len(clause) < clause_size:
            variable = random.randint(1,num_vars)
            sign = random.choice((-1, 1))
            clause.add(sign * variable)

        cnf.append(frozenset(clause))

    return cnf

# ==========================================================
# Utilities
# ==========================================================

def is_tautology(clause: Clause) -> bool:
    return any(
        -literal in clause
        for literal in clause
    )

def simplify_cnf(cnf: CNF) -> CNF:

    unique_clauses = {
        clause
        for clause in cnf
        if not is_tautology(clause)
    }

    return list(unique_clauses)

# ==========================================================
# Variable Selection
# ==========================================================

def choose_variable(
    cnf: CNF,
) -> Variable:

    frequencies = Counter(
        abs(literal)
        for clause in cnf
        for literal in clause
    )
    return frequencies.most_common(1)[0][0]

def assign_literal(
    cnf: CNF,
    literal: Literal,
) -> CNF:
    simplified: CNF = []
    for clause in cnf:
        if literal in clause:
            continue
        new_clause = frozenset(
            lit
            for lit in clause
            if lit != -literal
        )
        simplified.append(new_clause)

    return simplified

# ==========================================================
# Benchmark
# ==========================================================

@timed
def benchmark(
    method: Callable[[CNF], bool], 
    r: Iterable = range(2,30,2)
) -> None:
    
    print("\nBenchmark SAT Solver\n")
    for vars_count in r:
        print("-" * 50)
        print(f"Variables: {vars_count}")
        cnf = random_cnf(
            num_vars=vars_count,
            num_clauses=vars_count * 4,
            clause_size=3,
        )
        sat = method(cnf)
        print(f"Result: {'SAT' if sat else 'UNSAT'}")

# ==========================================================
# Dimacs
# ==========================================================

def load_dimacs(path: str) -> CNF:
    cnf = []
    with open(path) as fp:
        for line in fp:
            line = line.strip()
            if (
                not line
                or line.startswith("c")
                or line.startswith("p")
            ):
                continue

            clause = frozenset(
                int(x)
                for x in line.split()
                if x != "0"
            )
            cnf.append(clause)

    return cnf