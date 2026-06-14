from dataclasses import dataclass
from type_alias import Literal

@dataclass
class TrailEntry:
    literal: Literal
    level: int
    antecedent: frozenset[int] | None