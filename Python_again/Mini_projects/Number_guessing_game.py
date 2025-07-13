#1.Number guessing game
import random

start = int(input("Enter the start range: "))
end = int(input("Enter the end range: "))

chosen_number = random.randint(start, end)
print(chosen_number)


def guess_number():
    choice = None
    while choice != chosen_number:
        choice = int(input("Guess the number: "))
        print("Too low" if choice < chosen_number else "Too high")
    else:
        return "Correct!"

print(guess_number())
