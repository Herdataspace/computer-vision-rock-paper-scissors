# Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. <br>

**Rock beats scissors. Scissors beats paper. Paper beats rock.**  

This is an implementation of an interactive Rock-Paper-Scissors game, created using Python, in which the user can play with the computer using their webcam camera. 

Project completed as part of my training with <a href="https://www.theaicore.com/">**AiCORE**</a>. 

<br>

## Milestone 1 : Set up the environment

Git is a version control system that lets you keep track of your code history. The changes are saved to a remote GitHub repository. A GitHub remote repo is made, which is then cloned locally. 

```python
git clone https://github.com/Herdataspace/computer-vision-rock-paper-scissors.git
```

<br>

## Milestone 2 : Create the computer vision system

A computer-vision system, or model, is created using *'Teachable-Machine'*, which is able to detect whether the user is showing Rock, Paper or Scissors to the camera.  

An image model is created using four different classes:
- Rock
- Paper
- Scissors
- Nothing (represents the lack of option in the image)

<br>

Each class contains 200 image samples of a user showing the corresponding option. 

The model is then trained, with a batch size of 16 and an epoch of 50 - meaning that the model will work through the entire training dataset 50 times, with 16 samples used for 1 iteration of training. 

The accuracy of the model is shown here:

    | Class   | Accuracy | # Samples |
    | -----   | -----    | -----     |
    | Rock    | 1.00     | 30        |
    | Paper   | 0.93     | 30        |
    | Scissors| 1.00     | 30        |
    | Nothing | 1.00     | 30        |

The model is downloaded into *keras_mode.h5*, and a *labels.txt* file which includes the labels. These contain the structure and parameters of the deep-learning model.

These files are pushed to the remote GitHub repo.

<br>

## Milestone 3 : Install the dependencies

A new virtual environment is made, and pip is used to install the dependencies for the project inc.: *opencv-python*, *tensorflow*, and *ipykernel*

```python
conda create -n my_env python=3.8
conda install pip 
pip install tensorflow
```

<br>

## Milestone 4 : Create the game

The Rock-Paper-Scissors games is coded in Python manually. <br>
The code asks the user for an input, then compares the user input with the computer choice's to show a winner.<br>
This code is stored in the *manual_rps.py* file.

<br>

The **input** function is used to create user input:

```python
    user_choice = input('Rock, Paper, Scissors? ')
```
<br>

The **random** module is used to pick a random option between Rock, Paper and Scissors for the computer choice.

```python
possible_choices = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(possible_choices)
```
<br>

**If-elif-else** statements are used in a function to determine a winner, based on the classic rules of Rock-Paper-Scissors.  The function takes 2 arguments: *computer_choice* and *user_choice*.

The function prints the outcome of game: 

'You won!', 'You lost' or 'It is a tie!'

<br>

To simulate the game, a single function '*play*' calls the other 3 functions

<br> 

**Playing the game**:

![RPS_lost](https://github.com/Herdataspace/computer-vision-rock-paper-scissors/assets/117936304/aeb46c66-69cd-4b3b-8ae3-9e7ff3c0d5a5)

![RPS_tie](https://github.com/Herdataspace/computer-vision-rock-paper-scissors/assets/117936304/73391559-38d0-45cc-ab00-1436a70fc0ce)

![RPS_won](https://github.com/Herdataspace/computer-vision-rock-paper-scissors/assets/117936304/54c0a05d-5ee2-4734-bdc7-56b79715b31d)

<br>

## Milestone 5 : Use the camera to play Rock-Paper-Scissors

OpenCV is an open-source library that includes hundreds of computer vision algorithms. It is used in this project to capture an image of the user and determine their hand signal of choice - Rock/Paper/Scissors/Nothing. <br>

This output replaces the previously hard-coded user input. <br>

When the user shows a hand gesture to the camera, the model creates a numpy array of probabilities for each class. 
The model was trained in the order 'Rock', 'Paper', 'Scissors', and  'Nothing'. 
**'argmax'** returns the index of the class with the highest probability, which can then be used to determine the users hand signal.  <br>

The new code is stored in the *camera_rps.py* file. <br>
<br>

**Countdown**

A countdown timer is added to the webcam image, to indicate when the user should show their desired hand signal. 

The *time.time()* function is used to capture start and end times for the countdown. 
A while loop is then used to get how much time has passed since the script started:

```python
start_time = time.time()
timer = 15
end_time = start_time + timer

while time.time() < end_time:
```
```python
 if time.time() == start_time + 1:
            print(timer- 1)
            timer -= 1
            start_time += 1
            print(int(start_time + timer - time.time()))
```

![Screen Shot 2023-06-14 at 19 23 20](https://github.com/Herdataspace/computer-vision-rock-paper-scissors/assets/117936304/f067b324-089f-41a1-a9b3-5e11b13138d6)

<br>

**Continue playing until 3 victories**

The code is ammended to allow the game to continue until the player or computer wins three rounds, or 5 rounds have been played. 

*rounds_played*, *computer_wins* and *user_wins* are variables created to keep score of wins and rounds. <br>
A while loop is created to allow the game to continue until the user or computer wins 3 rounds. <br>
The game then prints the final score and determines the overall winner. 

**Play again?**

A new function is created to ask the user, at the end of the game, if they want to play again.

**Taking it further...**

To improve the readability of the code, the functions are put into the class 'RPS', and the code is separated into smaller functions. An instance of the class is then called in the play function. 

Further text is added to the frame to improve the user experience!


