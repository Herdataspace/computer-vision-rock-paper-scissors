import cv2
import random
from keras.models import load_model
import numpy as np
import time

def get_prediction():
    #Load the model
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Set the timer for the countdown
    start_time = time.time()
    timer = 15
    end_time = start_time + timer

    # Run a capture countdown
    while time.time() < end_time:
        if time.time() == start_time + 1:
            print(timer- 1)
            timer -= 1
            start_time += 1
            print(int(start_time + timer - time.time()))
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        #  Create text to be displayed on the image
        roundtext = f"Round {rounds_played}, get ready!"
        countdowntext = str(int(start_time + timer - time.time()))
        preparetext = f"Prepare to show rock, paper, or scissors in:"
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, roundtext, (50,50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, countdowntext, (600,400), font, 4, (0, 0, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, preparetext, (50,100), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        user_choice_prediction = np.argmax(prediction)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()

    # Destroy all the windows
    # cv2.destroyAllWindows()
    
    # Determine the user choice from the prediction
    if user_choice_prediction == 0:
        user_choice = 'Rock'
        print(f"You chose '{user_choice}'")
    elif user_choice_prediction == 1:
        user_choice = 'Paper'
        print(f"You chose '{user_choice}'")
    elif user_choice_prediction == 2:
        user_choice = 'Scissors'
        print(f"You chose '{user_choice}'")
    else:
        user_choice = 'Nothing'
        print(f"You chose '{user_choice}'")
    
    return user_choice

def get_computer_choice():
    possible_choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(possible_choices)
    return computer_choice

def get_user_choice():
    user_choice = get_prediction()
    return user_choice

def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        global winner 
        winner = user_choice, computer_choice
        print(f"The computer also chose: {computer_choice}. This round is a tie!" )
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            winner = user_choice
            print(f"The computer chose: {computer_choice}. You won this round!")
        elif user_choice == "Scissors":
            winner = computer_choice
            print(f"The computer chose: {computer_choice}. You lost this round!")
        elif user_choice == "Nothing":
            winner = computer_choice
            print('Please choose either Rock, Paper or Scissors.')
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            winner = user_choice
            print(f"The computer chose: {computer_choice}. You won this round!")
        elif user_choice == "Rock":
            winner = computer_choice
            print(f"The computer chose: {computer_choice}. You lost this round!")
        elif user_choice == "Nothing":
            winner = computer_choice
            print('Please choose either Rock, Paper or Scissors.')
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            winner = user_choice
            print(f"The computer chose: {computer_choice}. You won this round!")
        elif user_choice == "Paper":
            winner = computer_choice
            print(f"The computer chose: {computer_choice}. You lost this round!")
        elif user_choice == "Nothing":
            winner = computer_choice
            print('Please choose either Rock, Paper or Scissors.')
    return winner

def play():
    global rounds_played
    rounds_played = 1
    computer_wins = 0
    user_wins = 0
    # Continue playing until user or computer wins three rounds
    while computer_wins < 3 and user_wins < 3:
        print(f'Round : {rounds_played}, get ready!')
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)
        rounds_played += 1
        if winner == computer_choice:
            computer_wins += 1
        elif winner == user_choice:
            user_wins += 1
        else:
            computer_wins += 1
            user_wins += 1

        print(f'The final score is: \n computer - {computer_wins} \n user - {user_wins}')
        if computer_wins > user_wins:
            print('Better luck next time!')
        elif computer_wins < user_wins:
            print('Congratulations! You beat the computer!')
        else:
            print("It's a tie!")
           

def play_again():
    while True:
        play()
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break

play_again()