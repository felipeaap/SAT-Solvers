"""
dpll.py

Didactic DPLL implementation.
"""

from cnf import choose_variable, assign_literal

from helpers import timed

from .observer import DPLLSolverObserver
from type_alias import CNF

def unit_propagate(
    cnf: CNF,
    observer: DPLLSolverObserver | None = None,
) -> CNF:
    while True:
        unit_literal = next(
            (
                next(iter(clause))
                for clause in cnf
                if len(clause) == 1
            ),
            None,
        )
        if unit_literal is None:
            return cnf
        if observer:
            observer.on_unit_propagation(
                unit_literal
            )
        cnf = assign_literal(
            cnf,
            unit_literal,
        )

def pure_literal_elimination(
    cnf: CNF,
    observer: DPLLSolverObserver | None = None,
) -> CNF:
    literals = {
        literal
        for clause in cnf
        for literal in clause
    }
    pure_literals = [
        literal
        for literal in literals
        if -literal not in literals
    ]
    for literal in pure_literals:
        if observer:
            observer.on_pure_literal(
                literal
            )
        cnf = assign_literal(
            cnf,
            literal,
        )

    return cnf

# ==========================================================
# DPLL CORE
# ==========================================================

def dpll_recursive(
    cnf: CNF,
    observer: DPLLSolverObserver | None = None,
    depth: int = 0,
) -> bool:
    if observer:
        observer.on_recursive_call(depth, cnf)

    cnf = unit_propagate(cnf, observer)
    cnf = pure_literal_elimination(cnf, observer)

    if not cnf:
        return True
    
    if frozenset() in cnf:
        return False
    
    variable = choose_variable(cnf)
    if observer:
        observer.on_decision(variable)
        
    if dpll_recursive(
        assign_literal(cnf, variable),
        observer,
        depth + 1,
    ):
        return True
    
    if observer:
        observer.on_backtrack(variable)

    return dpll_recursive(
        assign_literal(cnf, -variable),
        observer,
        depth + 1,
    )

@timed
def dpll_sat(
    cnf: CNF,
    observer: DPLLSolverObserver | None = None,
) -> bool:
    result = dpll_recursive(cnf, observer)
    return result