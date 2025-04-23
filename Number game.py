# 🎮 Random Number Guessing Game 🎮
#
import random
# define constants
min_number = 1
# highest number
max_number =  600
# maximum number of guesses
max_guess = 8
#
# number game parameters
def number_game():
    random_number = int(random.triangular(min_number, max_number + 1, max_number))
    attempt_number = 0
    correct_guess = False
    print(f'i have picked a number between {min_number} and {max_number}.')
    print(f'you have {max_guess} tries to guess correctly.')
#
# main program
    while attempt_number < max_guess:
        try:
            attempt = attempt = int(input(f'round #{attempt_number + 1} - input number: '))
        except ValueError:
            print('invalid value.')
            continue
        if attempt < min_number or attempt > max_number:
            print(f'input must be between {min_number} and {max_number}. try again.')
            continue
        attempt_number += 1
# hint message for user 
        if attempt < random_number:
            print('too low, guess again.')
        elif attempt > random_number:
            print('too high, guess again.')
        else:
            print(f'correct. {random_number} tries to guess correctly.')
            correct_num = True
            break
    if not correct_guess:
        print(f'user is at maxinum number of guesses. the correct number was {random_number}.')
#
# main loop
while True:
    number_game()
    play_again = input('would you like to play again? ').strip().lower()
    if play_again not in ['y', 'yes']:
        print('thanks for playing my random number guessing game.')
        break
#
print('program ends.')
