import random

def get_computer_choice():
    possible_choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(possible_choices)
    print(f'Computer chose: {computer_choice}.')
    return computer_choice

def get_user_choice():
    user_choice = input('Rock, Paper, Scissors? ')
    return user_choice

def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print("It is a tie!" )
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
        elif user_choice == "Scissors":
            print("You lost")
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
        elif user_choice == "Rock":
            print("You lost")
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You won!")
        elif user_choice == "Paper":
            print("You lost")

# add a winner after each? then return winnner at end?

def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)