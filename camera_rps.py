import cv2
import random
from keras.models import load_model
import numpy as np
import time

class RPS():
    def __init__(self):
        self.rounds_played = 1
        self.computer_wins = 0
        self.user_wins = 0
        self.winner = None

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        # Set the timer for the countdown
        start_time = time.time()
        timer = 10
        end_time = start_time + timer
        while time.time() < end_time:
            ret, frame = cap.read()
             #  Text to be displayed on the image
            roundtext = f"Round {self.rounds_played}, get ready!"
            countdowntext = str(int(start_time + timer - time.time()))
            preparetext = f"Prepare to show rock, paper, or scissors in:"
            scoretext = f"Score: user- {self.user_wins} computer- {self.computer_wins}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            frame = cv2.putText(frame, roundtext, (50,50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            frame = cv2.putText(frame, countdowntext, (600,400), font, 4, (0, 0, 255), 2, cv2.LINE_AA)
            frame = cv2.putText(frame, preparetext, (50,100), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
            frame = cv2.putText(frame, scoretext, (50,600), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
            # Display the resulting frame
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        return frame
      
    def get_prediction(self, frame):
        #Load the model
        model = load_model('keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        # determine user choice from model
        user_choice_prediction = np.argmax(prediction)
        choices = ['Rock', 'Paper', 'Scissors', 'Nothing']
        user_choice = choices[user_choice_prediction]
        print(f"You chose '{user_choice}'")
        return user_choice    

    def get_computer_choice(self):
        possible_choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(possible_choices)
        return computer_choice

    def get_user_choice(self, frame):
        user_choice = self.get_prediction(frame)
        return user_choice

    def get_winner(self, computer_choice, user_choice):
        winning_combinations = {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
        }
        if user_choice == 'Nothing':
            print("Please choose either Rock, Paper or Scissors.")
            self.winner = None
        elif user_choice == computer_choice:
            self.winner = None
            print(f"The computer also chose: {computer_choice}. This round is a tie!")
        elif winning_combinations[user_choice] == computer_choice:
            self.winner = user_choice
            print(f"The computer chose: {computer_choice}. You won this round!")
        else:
            self.winner = computer_choice
            print(f"The computer chose: {computer_choice}. You lost this round!")

        return self.winner

def play():
    game = RPS()
    captured_frame = None
    # Continue playing until the user or computer wins three rounds or 5 rounds have been played
    while game.computer_wins < 3 and game.user_wins < 3 and game.rounds_played < 6:
        print(f'Round: {game.rounds_played}, get ready!')
        frame = game.capture_image()  # Capture the image
        captured_frame = frame  # Store the captured frame
        user_choice = game.get_user_choice(frame)  # Pass the captured frame
        computer_choice = game.get_computer_choice()
        winner = game.get_winner(computer_choice, user_choice)
        game.rounds_played += 1
        if winner == computer_choice:
            game.computer_wins += 1
        elif winner == user_choice:
            game.user_wins += 1
    
    win_text = 'Congratulations, you beat the computer!'
    loser_text = 'You lost! Better luck next time!'
    no_winner_text = 'Try again to get 3 victories!'

    print('\n------------------------------')
    print('           GAME OVER          ')
    print('------------------------------\n')
    print(f'The final score is: \n computer - {game.computer_wins} \n user - {game.user_wins}')
    if game.computer_wins == 3:
        print(loser_text) 
    elif game.user_wins == 3:
        print(win_text)
    else:
        print(no_winner_text)

    # Display game over message on the final captured frame
    game_over_text = "GAME OVER" 
    font = cv2.FONT_HERSHEY_SIMPLEX
    captured_frame = cv2.putText(captured_frame, game_over_text, (250, 400), font, 4, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', captured_frame)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
 
def play_again():
    while True:
        play()
        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() != 'y':
            break

play_again()