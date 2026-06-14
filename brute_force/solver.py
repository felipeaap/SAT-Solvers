"""
bruteforce_sat.py
"""


from itertools import product
from helpers import timed
from type_alias import Clause, Assignment, CNF


def evaluate_clause(
    clause: Clause,
    assignment: Assignment,
) -> bool:
    return any(
        assignment[abs(literal)] == (literal > 0)
        for literal in clause
    )


def evaluate_cnf(
    cnf: CNF,
    assignment: Assignment,
) -> bool:
    return all(
        evaluate_clause(clause, assignment)
        for clause in cnf
    )


def variable_count(cnf: CNF) -> int:
    return max(
        abs(literal)
        for clause in cnf
        for literal in clause
    )


@timed
def brute_force_sat(cnf: CNF) -> bool:
    n_vars = variable_count(cnf)

    for values in product((False, True), repeat=n_vars):
        assignment: Assignment = {
            var: value
            for var, value in enumerate(values, start=1)
        }

        if evaluate_cnf(cnf, assignment):
            return True

    return False