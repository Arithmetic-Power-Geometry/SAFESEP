# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from dataclasses import dataclass
from typing import Hashable, Mapping, FrozenSet

World = Hashable
Decision = Hashable
Outcome = Hashable

@dataclass(frozen=True)
class Experiment:
    name: str
    cost: float
    outcomes: Mapping[World, Outcome]
    admissible: FrozenSet[World]

    def outcome(self, world: World) -> Outcome:
        return self.outcomes[world]

    def is_admissible_on(self, worlds: FrozenSet[World]) -> bool:
        return worlds.issubset(self.admissible)

@dataclass(frozen=True)
class Problem:
    worlds: FrozenSet[World]
    decisions: Mapping[World, Decision]
    experiments: tuple[Experiment, ...]

    def decision_homogeneous(self, worlds: FrozenSet[World]) -> bool:
        return len({self.decisions[w] for w in worlds}) <= 1
