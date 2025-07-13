import random
order_of_inputs = []

def first_turn():
    user_turn(order_of_inputs)
    computer_turn(order_of_inputs)
    return order_of_inputs

def second_turn():
    computer_turn(order_of_inputs)
    user_turn(order_of_inputs)
    return order_of_inputs

def user_turn(order_of_inputs):
    number_of_inputs = int(input("How many numbers would you like to add?\n: "))
    print("Enter your values: \n")
    for _ in range(1, number_of_inputs + 1):
        order_of_inputs.append(int(input()))

def computer_turn(order_of_inputs):
    computer_input_number = random.randint(1, 21 - len(order_of_inputs))
    for num in range(len(order_of_inputs) + 1,
                     (len(order_of_inputs) + computer_input_number + 1)):
        order_of_inputs.append(num)
    print("Order of inputs after computer's turn is: ", order_of_inputs)


def count_to_21():
    turn = input("Enter 'F' for first chance\nEnter 'S' for second chance\n").lower()

    while len(order_of_inputs) != 21:
        if turn == "f":
            first_turn()
        elif turn == "s":
            computer_turn()

print("Player 2 is computer\n")
if input("Do you want to start the game? (y/n): \n").lower() == "y":
    count_to_21()
else: "Bye"