from dataclasses import dataclass

from .observer import DPLLSolverObserver
from type_alias import CNF, Variable, Literal

# ==========================================================
# STATS
# ==========================================================

@dataclass(slots=True)
class DPLLStats(DPLLSolverObserver):

    recursive_calls: int = 0
    decisions: int = 0
    backtracks: int = 0
    unit_propagations: int = 0
    pure_literal_assignments: int = 0
    
    def on_recursive_call( self, depth: int, cnf: CNF ) -> None: 
        self.recursive_calls +=1

    def on_unit_propagation( self, literal: Literal ) -> None: 
        self.unit_propagations += 1

    def on_pure_literal( self, literal: Literal ) -> None: 
        self.pure_literal_assignments += 1

    def on_decision( self, variable: Variable ) -> None: 
        self.decisions += 1

    def on_backtrack( self, variable: Variable ) -> None: 
        self.backtracks += 1

    def print(self):
        print("\n===== DPLL STATS =====")
        print(f"Recursive calls: {self.recursive_calls}")
        print(f"Decisions: {self.decisions}")
        print(f"Backtracks: {self.backtracks}")
        print(f"Unit propagations: {self.unit_propagations}")
        print(f"Pure literals: {self.pure_literal_assignments}")