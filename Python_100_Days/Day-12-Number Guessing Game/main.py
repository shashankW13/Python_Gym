import random

from art import logo

print(logo)
print('Welcome to the number guessing game!')
print('I am thinking of a number between 1 and 100')

og_number = random.randint(1, 100)
# print(f'{og_number}')

difficulty = input('Choose a difficulty - Type \'easy\' or \'hard\': ')

def play_game(level):
    attempts = 5 if level == 'hard' else 10

    while attempts > 0:
        print(f'You have {attempts} attempts left')
        num = int(input('Make a guess : '))

        if num == og_number:
            print(f'You got it! The answer was {og_number}')
            break
        elif num > og_number:
            print('Too high!')
            attempts -= 1
        else:
            print('Too low!')
            attempts -= 1
    else:
        print(f'You lose! Number was {og_number}')

play_game(difficulty)