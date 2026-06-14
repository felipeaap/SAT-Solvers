"""
CDCL Solver

Versão acadêmica baseada no DPLL existente.

Recursos:

- Unit Propagation
- Decision Levels
- Trail
- Conflict Detection
- Clause Learning
- Backjumping simplificado
"""

from cnf import choose_variable, assign_literal
from helpers import timed
from type_alias import CNF
from .observer import CDCLSolverObserver
from .classes import TrailEntry

def unit_propagate(
    cnf: CNF,
    trail: list[TrailEntry],
    level: int,
    observer: CDCLSolverObserver | None = None,
):

    while True:

        unit_clause = next(
            (
                clause
                for clause in cnf
                if len(clause) == 1
            ),
            None,
        )

        if unit_clause is None:
            return cnf, None

        literal = next(iter(unit_clause))

        trail.append(
            TrailEntry(
                literal=literal,
                level=level,
                antecedent=unit_clause,
            )
        )

        if observer:
            observer.on_unit_propagation(
                literal
            )

        cnf = assign_literal(
            cnf,
            literal
        )

        if frozenset() in cnf:
            return cnf, frozenset()


def analyze_conflict(trail: list[TrailEntry]):
    for entry in reversed(trail):
        if entry.antecedent is None:
            return frozenset([-entry.literal])

    return frozenset()


def backjump(trail: list[TrailEntry]) -> int:
    if not trail:
        return 0

    highest_level = max(
        entry.level
        for entry in trail
    )

    trail[:] = [
        entry
        for entry in trail
        if entry.level < highest_level
    ]

    if not trail:
        return 0

    return max(
        entry.level
        for entry in trail
    )


def cdcl_recursive(
    cnf: CNF,
    trail: list[TrailEntry],
    level: int,
    observer: CDCLSolverObserver | None = None,
) -> bool:
    cnf, conflict = unit_propagate(
        cnf,
        trail,
        level,
        observer
    )
    if not cnf:
        return True
    
    if conflict is not None:

        if observer:
            observer.on_conflict(
                conflict
            )

        learned_clause = analyze_conflict(
            trail
        )

        if observer:
            observer.on_clause_learned(
                learned_clause
            )

        cnf.append(
            learned_clause
        )

        jump_level = backjump(
            trail
        )

        if observer:
            observer.on_backjump(
                level,
                jump_level,
            )

        return False
    
    variable = choose_variable(
        cnf
    )

    if observer:
        observer.on_decision(
            variable,
            level + 1,
        )

    trail.append(
        TrailEntry(
            literal=variable,
            level=level + 1,
            antecedent=None,
        )
    )

    if cdcl_recursive(
        assign_literal(
            cnf,
            variable
        ),
        trail,
        level + 1,
        observer,
    ):
        return True

    trail.append(
        TrailEntry(
            literal=-variable,
            level=level + 1,
            antecedent=None,
        )
    )

    return cdcl_recursive(
        assign_literal(
            cnf,
            -variable
        ),
        trail,
        level + 1,
        observer,
    )


@timed
def cdcl_sat(
    cnf: CNF,
    observer: CDCLSolverObserver | None = None,
) -> bool:

    trail: list[TrailEntry] = []

    return cdcl_recursive(
        cnf,
        trail,
        0,
        observer,
    )