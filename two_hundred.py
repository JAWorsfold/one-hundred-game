# Joseph Worsfold - jworsf01
# Executes the two-hundred game - see instructions for more details

import random


def instructions():
    """Tells the user the rules of the game."""
    # add something to make it look nicer
    print('Welcome to the "Hundred" game.\nThe aim of the game is to be the '
          'first to reach a score of 100.\nEach turn you will roll a six '
          'sided die and add the result to\nyour score. However, if you roll '
          'a 1 your score for that turn will\nbe 0. You will play against the'
          ' computer who will roll first.')
    #  use the %s method to add the nicer layout


def computer_move(computer_score, human_score):
    """The computer rolls a random number of times, displays the result of
    each roll, and returns the result (either 0 or the total of the rolls)."""
    print(' \nThis is the computer\'s turn:')
    roll_total = 0
    if computer_score >= human_score:
        while roll_total < 11:
            roll_score = roll_calc(roll())
            if roll_score == 0:
                print('The computer\'s score at the end of the turn is 0.')
                return 0
            roll_total += roll_score
        print('The computer\'s score at the end of the turn is '
              + str(roll_total) + '.')
        return roll_total
    # elif computer_score < human_score - human_score * 0.3:
    #     while (computer_score + roll_total < human_score - human_score * 0.25
    #            or roll_total > 11):
    #         roll_score = roll_calc(roll())
    #         if roll_score == 0:
    #             print('The computer\'s score at the end of the turn is 0.')
    #             return 0
    #         roll_total += roll_score
    #     print('The computer\'s score at the end of the turn is '
    #           + str(roll_total) + '.')
    #     return roll_total
    else:
        while roll_total < 17:
            roll_score = roll_calc(roll())
            if roll_score == 0:
                print('The computer\'s score at the end of the turn is 0.')
                return 0
            roll_total += roll_score
        print('The computer\'s score at the end of the turn is '
              + str(roll_total) + '.')
        return roll_total

    # num_of_rolls = random.randint(1, 6)
    # while num_of_rolls != 0:
    #     roll_score = roll_calc(roll())
    #     if roll_score == 0:
    #         return roll_score
    #         print('The computer\'s score at the end of the turn is 0.')
    #     roll_total += roll_score
    #     num_of_rolls -= 1
    # print('The computer\'s score at the end of the turn is '
    #       + str(roll_total) + '.')
    # return roll_total


# def computer_ai(computer_score, human_score):
# This works out if True or False for next roll
# def computer_ai_setting?
# This works out if it'll play agrressive, conservative, or safe


def human_move(computer_score, human_score):
    """Tells the user both their current score and the computer's score, and
    how far behind (or ahead) they are. Then repeatedly asks whether the user
    wants to roll again."""
    print(' \nYour current score is ' + str(human_score) + ', and the '
          'computer\'s score is ' + str(computer_score) + '.')
    diff = abs(computer_score - human_score)
    if human_score > computer_score:
        print('You\'re ahead by ' + str(diff) + '.')
    elif human_score < computer_score:
        print('You\'re behind by ' + str(diff) + '.')
    else:
        print('You\'re tied at ' + str(human_score) + '.')
    print(' \nNow it\'s your turn:')
    new_turn = True
    roll_total = 0
    while new_turn:
        roll_score = roll_calc(roll())
        if roll_score == 0:
            print('The score at the end of your turn is 0.')
            return roll_score
        roll_total += roll_score
        new_turn = ask_yes_or_no(input('Roll again? (y/n): '))
    print('The score at the end of your turn is ' + str(roll_total) + '.')
    return roll_total


def roll_calc(roll):
    """If roll equals 1, score equals 0. Otherwise roll score equals roll."""
    print(roll)
    if roll == 1:
        return 0
    return roll


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
    """Returns True if either player has 100 or more, and the players are
    not tied, otherwise it returns False."""
    if human_score != computer_score and (human_score >= 100 or
                                          computer_score >= 100):
        return True
    else:
        return False


def show_results(computer_score, human_score):
    """Tells whether the human won or lost, and by how much."""
    diff = abs(human_score - computer_score)
    if computer_score > human_score:
        print('Unlucky, the computer won with a score of ' +
              str(computer_score) + '. Beating you by ' + str(diff) + '.')
    else:
        print('Congratulations, you won with a score of ' + str(human_score)
              + '. Beating the computer by ' + str(diff) + '.')


def main():
    """This is where the program will be executed."""
    computer_score = 0
    human_score = 0
    instructions()
    while not is_game_over(computer_score, human_score):
        computer_score += computer_move(computer_score, human_score)
        human_score += human_move(computer_score, human_score)
        is_game_over(computer_score, human_score)
    show_results(computer_score, human_score)


if __name__ == '__main__':
    main()
