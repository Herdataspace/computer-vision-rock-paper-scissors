import random

def get_computer_choice():
    rps_choice = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(rps_choice)
    return computer_choice

def get_user_choice():
    user_choice = input('Rock, Paper, Scissors? ')
    return user_choice