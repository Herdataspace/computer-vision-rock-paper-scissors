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

