import random

def get_computer_choice():
    possible_choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(possible_choices)
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
            return user_choice
        if user_choice == "Scissors":
            print("You lost!")
            return computer_choice
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
            return user_choice
        if user_choice == "Rock":
            print("You lost!")
            return computer_choice
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You won!")
            return user_choice
        if user_choice == "Paper":
            print("You lost!")
            return computer_choice