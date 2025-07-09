# Rock, Paper, Scissors (Python)

This is a simple Python implementation of the classic game **Rock, Paper, Scissors**, completed as part of the [Codecademy Learn Python](https://www.codecademy.com/courses/learn-python/) course.

## 🎯 Project Overview

This command-line game allows a user to play Rock, Paper, Scissors against the computer. The program randomly selects a move for the computer and compares it to the user's choice to determine the winner.

This project was designed to reinforce core Python concepts:
- `input()` and user interaction
- `if`/`elif`/`else` conditionals
- comparison operators
- string manipulation
- random number generation with the `random` module
- functions and basic code organization


## 📄 Code for the project:

```python
"""
CodeCademy
Play rock - paper - scissors
"""
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {"tie": "Yawn it's a tie","won":"Yay you won!","lost":"Aww you lost"}

def decide_winner(user_choice, computer_choice):
  print "Your choice is: %s" % user_choice
  print "The computer chose: %s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()

```

✅ Features
 - Basic input validation
 - Randomized computer moves
 - Clear output to indicate results
 - Easily extendable (e.g. add score tracking, best-of rounds, etc.)

🧠 Skills Practiced
 - Writing clean and readable code
 - Handling user input and program flow
 - Implementing game logic using conditionals
 - Using Python's standard library

🛠️ Possible Improvements
 - Loop the game until the user chooses to quit
 - Track and display scores over multiple rounds


