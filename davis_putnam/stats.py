"""
stats.py
"""

from dataclasses import dataclass

from .observer import DPSolverObserver
from type_alias import CNF, Variable


@dataclass(slots=True)
class DPStats(DPSolverObserver):
    resolutions: int = 0
    variables_eliminated: int = 0

    max_clauses: int = 0
    max_clause_size: int = 0

    initial_clauses: int = 0
    final_clauses: int = 0

    def on_start(self,cnf: CNF) -> None:
        self.initial_clauses = len(cnf)

    def on_iteration(self, cnf: CNF) -> None:
        self.max_clauses = max(self.max_clauses, len(cnf))
        if cnf:
            self.max_clause_size = max(
                self.max_clause_size,
                max(len(clause) for clause in cnf)
            )

    def on_variable_eliminated(self, variable: Variable) -> None:
        self.variables_eliminated += 1

    def on_resolution(self) -> None:
        self.resolutions += 1

    def on_finish(self, result: bool, cnf: CNF) -> None:
        self.final_clauses = len(cnf)

    def print(self) -> None:
        print("\n===== STATISTICS =====")
        print(f"Variables eliminated: {self.variables_eliminated}")
        print(f"Resolutions performed: {self.resolutions}")
        print(f"Initial clauses: {self.initial_clauses}")
        print(f"Final clauses: {self.final_clauses}")
        print(f"Maximum simultaneous clauses: {self.max_clauses}")
        print(f"Largest clause size: {self.max_clause_size}")