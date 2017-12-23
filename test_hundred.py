from hundred import *
import random
import sys


# I guess I can't test main() because it doesn't return anything...?


def test_human_move():
    sys.stdin = open("inputs.txt")
    random.seed(1)
    assert human_move(0, 0) == 0
    sys.stdin = open("inputs.txt")
    random.seed(3)
    assert human_move(0, 0) == 12
    sys.stdin = open("inputs.txt")
    random.seed(5)
    assert human_move(0, 0) == 14


def test_computer_move():
    random.seed(1)
    assert computer_move(0, 0) == 0  # tests 'safe' playing computer
    random.seed(1)
    assert computer_move(0, 100) == 0  # tests 'agressive' computer
    random.seed(3)
    assert computer_move(0, 0) == 12  # tests 'safe' computer
    random.seed(3)
    assert computer_move(0, 100) == 17   # tests 'agressive' computer
    random.seed(5)
    assert computer_move(0, 0) == 14  # tests 'safe' computer
    random.seed(5)
    assert computer_move(0, 100) == 17   # tests 'agressive' computer


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
    assert roll() >= 0

# I used the below code to see sequences of random numbers, based on a seed #


# def roll_seed():
#     return random.randint(1, 6)
#
#
# random.seed(5)
# result = 0
# for i in range(5):
#     roll = roll_seed()
#     print(roll)
#     result += roll
# print(result)
