from two_hundred import *


def test_ask_yes_or_no():
    assert ask_yes_or_no('Y') == True
    assert ask_yes_or_no('y') == True
    assert ask_yes_or_no('N') == False
    assert ask_yes_or_no('n') == False


def test_is_game_over():
    assert is_game_over(100, 100) == False
    assert is_game_over(200, 200) == False
    assert is_game_over(100, 0) == True
    assert is_game_over(0, 0) == False
    assert is_game_over(0, 100) == True


def test_roll():
    assert roll() <= 6
    assert roll() > 0

# possibly get rid of this after refactoring


def test_roll_calc():
    assert roll_calc(roll()) <= 6
    assert roll_calc(roll()) >= 0

# add test for the major functions - computer and human move
# Work out how to use a random seed
# Can I test the move now as I've added lots of print statements? Yes...
