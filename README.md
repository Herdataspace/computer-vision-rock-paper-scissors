# Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. 
Rock beats scissors. Scissors beats paper. Paper beats rock. 

The player who shows the first option that beats the other player's option wins. 

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

<br>

## Milestone 1

- Git is a version control system that lets you keep track of your code history. The changes are saved to a remote GitHub repository. A GitHub remote repo is made, which is then cloned locally. 

```python
git clone https://github.com/Herdataspace/computer-vision-rock-paper-scissors.git
```

<br>

## Milestone 2

- A computer-vision system, or model, is created using *'Teachable-Machine'*, which is able to detect whether the user is showing Rock, Paper or Scissors to the camera.  

- An image model is created using four different classes:
    - Rock
    - Paper
    - Scissors
    - Nothing (represents the lack of option in the image)

<br>

- Each class contains 200 image samples of a user showing the corresponding option. 

- The model is then trained, with a batch size of 16 and an epoch of 50 - meaning that the model will work through the entire training dataset 50 times, with 16 samples used for 1 iteration of training. 

- The accuracy of the model is shown here:

    | Class   | Accuracy | # Samples |
    | -----   | -----    | -----     |
    | Rock    | 1.00     | 30        |
    | Paper   | 0.93     | 30        |
    | Scissors| 1.00     | 30        |
    | Nothing | 1.00     | 30        |

- The model is downloaded into *keras_mode.h5*, and a *labels.txt* file which includes the labels. These contain the structure and parameters of the deep-learning model.

- These files are pushed to the remote GitHub repo.

<br>

## Milestone 3

A new virtual environment is made, and pip is used to install the dependencies for the project inc.: *opencv-python*, *tensorflow*, and *ipykernel*

```python
conda create -n my_env python=3.8
conda install pip 
pip install tensorflow
```

<br>

## Milestone 4

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