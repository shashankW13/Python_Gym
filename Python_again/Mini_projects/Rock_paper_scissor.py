import random

print("Winning rules of the game ROCK PAPER SCISSORS are:")
print("Rock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins \nPaper vs Scissors -> Scissors wins\n ")

choices = ["rock", "paper", "scissors"]
result_list = {'12': 2, '13': 1, '23': 3,
               '21': 2, '31': 1, '32': 3,
               '11': 'Draw', '22': 'Draw', '33': 'Draw'}

def computer_choice(choice_list):
    comp_choice = random.randint(1, len(choice_list))
    return comp_choice

def start_game(choice_list, result_list):
    play_again = True
    user_win = 0
    computer_win = 0

    while play_again:
        print("Choose your option:")
        print("1-Rock\n2-Paper\n3-Scissors\n")

        user_choice = int(input(("Enter your choice:")))
        print(f"User's choice is: {choice_list[user_choice - 1]}\n")

        print("Now it's computer's turn: ")
        comp_choice = computer_choice(choice_list)
        print(f"Computer's choice is: {choice_list[comp_choice - 1]}\n")

        winner = result_list[str(user_choice) + str(comp_choice)]
        print(f"{choice_list[winner - 1]} WINS!") if type(winner) == int \
            else print(f"{winner}")
        if type(winner) == int:
            if choice_list[winner - 1].lower() == choice_list[user_choice - 1].lower():
                print("Congratulations, you won!")
                user_win += 1
            else:
                print("Computer won!")
                computer_win += 1

        print(f"\nUser wins: {user_win}\tComputer wins: {computer_win}\n")
        play = input("Do you want to play again? (y/n):\n")
        play_again = True if play.lower() == "y" else False

start_game(choices, result_list)



