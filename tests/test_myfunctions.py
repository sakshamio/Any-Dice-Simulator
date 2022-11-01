from anyDiceSimulator import myfunctions


def test_a_few_rolls():
    for roll_spec, expected_count, (roll_min, roll_max) in [
        ("3d10", 3, (1, 10)),
        ("2d6", 2, (1, 6)),
    ]:
        rolls, sum_of_rolls = myfunctions.roll(roll_spec)
        assert expected_count == len(rolls)
        assert all(roll_min <= roll <= roll_max for roll in rolls)
        assert roll_min * expected_count <= sum_of_rolls <= roll_max * expected_count
