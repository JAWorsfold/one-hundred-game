import random


def instructions():
    """Tells the user the rules of the game."""
    print('The instructions')


def computer_move(computer_score, human_score):
    """
    The computer rolls a random number of times, displays the result of each
    roll, and returns the result (either 0 or the total of
    the rolls).
    """
    num_of_rolls = random.randint(1, 6)
    roll_total = 0
    while num_of_rolls != 0:
        roll_num = roll()
        print(roll_num)
        if roll_num == 1:
            computer_score = 0
            return computer_score
        roll_total += roll_num
        num_of_rolls -= 1
    return roll_total


def human_move(computer_score, human_score):
    """
    Tells the user both her current score and the computer's score, and how
    far behind (or ahead) she is. Then repeatedly asks whether the user
    wants to roll again. This continues until either:

    -   The user decides not to roll again. The function should return the
        total of the rolls made during this move.
    -   The user rolls a 1. The function should return 0.``
    """
    print('Your current score is ' + str(human_score) + ', and the computer\'s'
          ' score is ' + str(computer_score) + '.')  # make this a function?
    diff = abs(computer_score - human_score)  # make this a function?
    if human_score > computer_score:  # make this a function?
        print('You\'re ahead by ' + str(diff) + '.')
    elif human_score < computer_score:
        print('You\'re behind by ' + str(diff) + '.')
    else:
        print('You\'re tied at ' + str(human_score) + '.')
    new_turn = ask_yes_or_no(input('Do you want to roll? (y/n): '))
    roll_total = 0
    while new_turn:
        roll_num = roll()
        print(roll_num)
        if roll_num == 1:
            human_score = 0
            return human_score
        roll_total += roll_num
        new_turn = ask_yes_or_no(input('Roll again (y/n): '))
    return roll_total


def roll():
    """Returns a random number in the range 1 to 6, inclusive."""
    return random.randint(1, 6)


def ask_yes_or_no(prompt):
    """Asks the player if they want to roll again."""
    if prompt == 'Y' or prompt == 'y':
        return True
    elif prompt == 'N' or prompt == 'n':
        return False
    else:
        return ask_yes_or_no(input('Invalid entry. Try again (y/n): '))


def is_game_over(computer_score, human_score):
    """
    Returns `True` if either player has 100 or more, and the players are
    not tied, otherwise it returns `False`. (Call this only after the
    human's move.)
    """
    if human_score != computer_score and (human_score >= 100 or
                                          computer_score >= 100):
        return True
    else:
        return False


def show_results(computer_score, human_score):
    """
    Tells whether the human won or lost, and by how much. (Call this
    when the game has ended.)
    """
    diff = abs(human_score - computer_score)
    if computer_score > human_score:
        print('Unlucky, the computer won with a score of ' +
              str(computer_score) + '. Beating you by ' + str(diff) + '.')
    else:
        print('Congratulations, you won with a score of ' + str(human_score)
              + '. Beating the computer by ' + str(diff) + '.')


def main():
    """This is where the program will start execution."""
    c = 0  # computer score
    h = 0  # human score
    instructions()
    stop_playing = is_game_over(c, h)
    while not stop_playing:
        c += computer_move(c, h)
        h += human_move(c, h)
        stop_playing = is_game_over(c, h)
    show_results(c, h)


if __name__ == '__main__':
    main()
