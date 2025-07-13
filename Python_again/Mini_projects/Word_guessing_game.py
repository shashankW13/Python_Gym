import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = 'geeks'
print(word)

print(f"Hi, {input("Enter your name: ")}"
      f"\nWelcome to Word Guessing Game!\n"
      f"Good luck!\n")

def guess_word(word):
    turns = len(word) + 2
    guess_list = ['_' for _ in range(len(word))]

    while turns > 0:
        print(f"Guess the Word\nTurns: {turns}\n{guess_list}")
        char = input("Guess a character: ").lower()

        if char in word.lower():
            for index, letter in enumerate(word):
                if letter == char:
                    guess_list[index] = char
            print(f"\nGuess the characters\nTurns: {turns}\n{guess_list}\n")
        else:
            turns -= 1
            print(f"\nGuess the characters\nTurns: {turns}\n{guess_list}\n")

        guessed_word = ''.join(guess_list)
        print(guessed_word)
        if guessed_word == word:
            return f"You won! The word was {guessed_word}!"
    else:
        return "All turns over\nYou lost!"


print(guess_word(word))





