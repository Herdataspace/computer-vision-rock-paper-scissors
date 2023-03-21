import cv2
import random
from keras.models import load_model
import numpy as np

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        user_choice_prediction = np.argmax(prediction)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(user_choice_prediction)
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    if user_choice_prediction == 0:
        user_choice = 'Rock'
        print(user_choice)
    elif user_choice_prediction == 1:
        user_choice = 'Paper'
        print(user_choice)
    elif user_choice_prediction == 2:
        user_choice = 'Scissors'
        print(user_choice)
    else:
        user_choice = 'Nothing'
        print(user_choice)
    
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
        winner = user_choice, computer_choice
        print(f"The computer also chose: {computer_choice}. It is a tie!" )
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            winner = user_choice
            print(f"The computer chose: {computer_choice}. You won!")
        elif user_choice == "Scissors":
            winner = computer_choice
            print(f"The computer chose: {computer_choice}. You lost")
        elif user_choice == "Nothing":
            winner = computer_choice
            print('Please choose either Rock, Paper or Scissors.')
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            winner = user_choice
            print(f"The computer chose: {computer_choice}. You won!")
        elif user_choice == "Rock":
            winner = computer_choice
            print(f"The computer chose: {computer_choice}. You lost")
        elif user_choice == "Nothing":
            winner = computer_choice
            print('Please choose either Rock, Paper or Scissors.')
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            winner = user_choice
            print(f"The computer chose: {computer_choice}. You won!")
        elif user_choice == "Paper":
            winner = computer_choice
            print(f"The computer chose: {computer_choice}. You lost")
        elif user_choice == "Nothing":
            winner = computer_choice
            print('Please choose either Rock, Paper or Scissors.')
    return winner

def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)

play()