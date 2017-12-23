# Joseph Worsfold - jworsf01
# Executes the two-hundred game - see instructions for more details

import random


def instructions():
    """Tells the user the rules of the game."""
    print('Welcome to the "Hundred" game.\nThe aim of the game is to be the '
          'first to reach a score of 100.\nEach turn you will roll a six '
          'sided die and add the result to\nyour score. However, if you roll '
          'a 1 your score for that turn will\nbe 0. You will play against the'
          ' computer who will roll first.')


def computer_move(computer_score, human_score):
    """The computer rolls a random number of times, displays the result of
    each roll, and returns the result (either 0 or the total of the rolls)."""
    print(' \nThis is the computer\'s turn:')
    roll_total = 0
    if computer_score >= human_score:
        while roll_total < 11:  # plays it slightly more safe
            roll_score = roll()
            if roll_score == 0:
                print('The computer\'s score at the end of the turn is 0.')
                return 0
            roll_total += roll_score
        print('The computer\'s score at the end of the turn is '
              + str(roll_total) + '.')
        return roll_total
    else:
        while roll_total < 17:  # aggressive but still gets results
            roll_score = roll()
            if roll_score == 0:
                print('The computer\'s score at the end of the turn is 0.')
                return 0
            roll_total += roll_score
        print('The computer\'s score at the end of the turn is '
              + str(roll_total) + '.')
        return roll_total


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
        roll_score = roll()
        if roll_score == 0:
            print('The score at the end of your turn is 0.')
            return roll_score
        roll_total += roll_score
        new_turn = ask_yes_or_no(input('Roll again? (y/n): '))
    print('The score at the end of your turn is ' + str(roll_total) + '.')
    return roll_total


def roll():
    """Calculates the roll's score based on a random number from 1 to 6."""
    roll = random.randint(1, 6)
    print('The roll was: ' + str(roll))
    if roll == 1:  # based on game parameters a roll of 1 == 0
        return 0
    return roll


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
