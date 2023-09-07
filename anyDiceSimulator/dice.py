import random
from typing import List, Optional

BUILDER_SIDE_COUNT_CHANGE_ERROR = (
    "Create a new DieBuilder if you need to change the side count"
)


class Die:
    def __init__(self, sides: List[int], weights: List[int]):
        assert len(sides) == len(weights)
        self.sides = sides
        self.weights = weights

    def roll(self, count: int = 1) -> "RollResult":
        rolls = random.choices(self.sides, k=count, weights=self.weights)
        return RollResult(rolls, self)

    def is_regular(self) -> bool:
        if len(self.weights) == 0:
            return True

        w = self.weights[0]
        return all(weight == w for weight in self.weights)

    def is_biased(self) -> bool:
        return not self.is_regular()


class RollResult:
    def __init__(self, rolls: List[int], die: Die):
        self.rolls = rolls
        self.die = die
        self.sum_of_rolls = sum(rolls)


def get_standard_sides(side_count: int) -> List[int]:
    return list(range(1, side_count + 1))


class DieBuilder:
    def __init__(
        self, sides: Optional[List[int]] = None, weights: Optional[List[int]] = None
    ):
        self.sides: List[int] = sides if isinstance(sides, list) else [1, 2, 3, 4, 5, 6]
        self.weights = [1 for _ in self.sides]
        if isinstance(weights, list):
            assert len(weights) == len(self.sides)
            self.weights = weights

    def build(self) -> Die:
        return Die(self.sides, self.weights)

    def with_sides(self, sides: List[int]) -> "DieBuilder":
        assert len(sides) == len(self.weights), BUILDER_SIDE_COUNT_CHANGE_ERROR
        return DieBuilder(sides, self.weights)

    def with_weights(self, weights: List[int]) -> "DieBuilder":
        assert len(weights) == len(self.sides), BUILDER_SIDE_COUNT_CHANGE_ERROR
        return DieBuilder(self.sides, weights)
