"""
davis_putnam.py

Classical Davis-Putnam (1960) algorithm.
"""
from type_alias import Clause, Variable, CNF

from cnf import is_tautology, simplify_cnf, choose_variable
from helpers import timed

from .observer import DPSolverObserver


# ==========================================================
# Resolution
# ==========================================================

def resolve(
    positive_clause: Clause,
    negative_clause: Clause,
    variable: Variable,
) -> Clause:

    return frozenset(
        literal
        for literal in (
            positive_clause | negative_clause
        )
        if literal not in (variable, -variable)
    )


# ==========================================================
# Variable Elimination
# ==========================================================

def eliminate_variable(
    cnf: CNF,
    variable: Variable,
    observer: DPSolverObserver | None = None,
) -> CNF:
    positive: list[Clause] = []
    negative: list[Clause] = []
    remaining: list[Clause] = []

    for clause in cnf:
        if variable in clause:
            positive.append(clause)
        elif -variable in clause:
            negative.append(clause)
        else:
            remaining.append(clause)

    resolvents: set[Clause] = set()
    for p_clause in positive:
        for n_clause in negative:
            if observer:
                observer.on_resolution()

            resolvent = resolve(
                p_clause,
                n_clause,
                variable,
            )

            if not is_tautology(resolvent):
                resolvents.add(resolvent)

    return simplify_cnf(remaining + list(resolvents))


# ==========================================================
# Solver
# ==========================================================

@timed
def davis_putnam_sat(
    cnf: CNF,
    observer: DPSolverObserver | None = None,
) -> bool:
    if observer:
        observer.on_start(cnf)

    while cnf:
        if observer:
            observer.on_iteration(cnf)

        if frozenset() in cnf:
            if observer:
                observer.on_finish(False, cnf)

            return False

        variable = choose_variable(cnf)
        if observer:
            observer.on_variable_eliminated(variable)

        cnf = eliminate_variable(
            cnf,
            variable,
            observer,
        )

    if observer:
        observer.on_finish(True, cnf)

    return True