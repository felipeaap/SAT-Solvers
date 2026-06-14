from dataclasses import dataclass

from .observer import CDCLSolverObserver
from type_alias import CNF, Literal

# ==========================================================
# STATS
# ==========================================================

@dataclass(slots=True)
class CDCLStats(CDCLSolverObserver):
    recursive_calls: int = 0
    max_decision_level: int = 0
    unit_propagations: int = 0
    learned_clauses: int = 0
    conflicts: int = 0
    decisions: int = 0
    backjumps: int = 0
    restarts: int = 0

    def on_recursive_call(self,level: int,cnf: CNF) -> None:
        self.recursive_calls += 1
        self.max_decision_level = max(
            self.max_decision_level,
            level,
        )

    def on_decision(self,literal: Literal,level: int) -> None:
        self.decisions += 1

    def on_unit_propagation(self,literal: Literal) -> None:
        self.unit_propagations += 1

    def on_conflict(self,clause: frozenset[int]) -> None:
        self.conflicts += 1

    def on_clause_learned(self,clause: frozenset[int]) -> None:
        self.learned_clauses += 1

    def on_backjump(self,from_level: int,to_level: int) -> None:
        self.backjumps += 1

    def on_restart(self) -> None:
        self.restarts += 1

    def on_clause_database_size(self,size: int) -> None:
        self.max_clause_database = max(
            self.max_clause_database,
            size,
        )

    def print(self):
        print("\n===== DPLL STATS =====")
        print(f"Recursive calls: {self.recursive_calls}")
        print(f"learned_clauses: {self.learned_clauses}")
        print(f"Unit propagations: {self.unit_propagations}")
        print(f"Max decision level: {self.max_decision_level}")
        print(f"Decisions: {self.decisions}")
        print(f"Backjumps: {self.backjumps}")
        print(f"Restarts: {self.restarts}")
        print(f"Conflicts: {self.conflicts}")