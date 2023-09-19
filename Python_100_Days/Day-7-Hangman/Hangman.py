import random
import Hangman_words
from Hangman_art import stages, logo

word_list = Hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1
end_of_game = False

print(f'word : {chosen_word}')

display = []

for letter in chosen_word:
    display.append('_')

print(logo)

while not end_of_game:
    guess = input("Guess letter : ")
    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            if guess == display[position]:
                print(f'Already guessed : {guess}')
            display[position] = guess
            if '_' not in display:
                end_of_game = True
                print('You win')

    if guess not in chosen_word:
        lives -= 1
        print(f'Letter : {guess} not in the word, You lose a life!')
        if lives == 0:
            end_of_game = True
            print('You lose')

    print(stages[lives])
    print(f'Lives : {lives}')
    for ele in display:
        print(ele, end=' ')
    print('\n')
