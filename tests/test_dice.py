from anyDiceSimulator import dice


def test_a_few_rolls():
    for side_count, is_biased, roll_count in [
        (6, False, 3),
        (10, True, 2),
    ]:
        sides = dice.get_standard_sides(side_count)
        weights = list(range(side_count)) if is_biased else None
        die = dice.DieBuilder(sides, weights).build()
        assert is_biased == die.is_biased()

        result = die.roll(roll_count)

        assert len(result.rolls) == roll_count
        assert all(1 <= roll <= side_count for roll in result.rolls)
