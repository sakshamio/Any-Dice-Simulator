from anyDiceSimulator import myfunctions


def testDice():
    x, y = myfunctions.roll('3d10')
    assert len(x) > 0
    assert y >= 0
