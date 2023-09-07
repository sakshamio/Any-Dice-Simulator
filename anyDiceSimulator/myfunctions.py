from random import randint
from typing import Tuple, List


def roll(roll_spec: str) -> Tuple[List[int], int]:
    rolled = []
    number_of_rolls, die_side_count = [int(substr) for substr in roll_spec.split("d")]
    try:
        for x in range(number_of_rolls):
            print(f"Rolling die {x + 1}...")
            result = randint(1, die_side_count)
            print(f"Result: {result}")
            rolled.append(result)
    except Exception as err:
        print(f"I got bungled @_@ \n Error: {err}")

    return rolled, sum(rolled)


def print_result(rolled: List[int], sum_of_rolls: int):
    print(f"You rolled {rolled} which has a total of {sum_of_rolls}")


def rolldice(roll_spec: str):
    rolled, sum_of_rolls = roll(roll_spec)
    print_result(rolled, sum_of_rolls)
