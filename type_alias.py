from typing import TypeAlias

Literal: TypeAlias = int
Variable: TypeAlias = int

Clause: TypeAlias = frozenset[Literal]
CNF: TypeAlias = list[Clause]

Assignment: TypeAlias = dict[int, bool]