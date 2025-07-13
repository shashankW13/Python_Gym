import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = 'geeks'
print(word)

print(f"Hi, {input("Enter your name: ")}"
      f"\nWelcome to Word Guessing Game!\n"
      f"Good luck!\n")

def guess_word(word):
    turns = len(HANGMANPICS)
    guess_list = ['_' for _ in range(len(word))]
    print(f"Guess the Word\nTurns: {turns}\n{guess_list}")
    print(HANGMANPICS[7 - turns])

    while turns > 0:
        char = input("Guess a character: ").lower()

        if char in word.lower():
            for index, letter in enumerate(word):
                if letter == char:
                    guess_list[index] = char
            print(f"\nGuess the characters\nTurns: {turns}\n{guess_list}")
            print(HANGMANPICS[7 - turns], "\n")
        else:
            turns -= 1
            print(f"\nGuess the characters\nTurns: {turns}\n{guess_list}\n")
            print(HANGMANPICS[7 - turns], "\n" if turns > 0 else "Dead!")

        guessed_word = ''.join(guess_list)
        print(guessed_word)
        if guessed_word == word:
            return f"You won! The word was {guessed_word}!"
    else:
        return "All turns over\nYou lost!"


print(guess_word(word))
