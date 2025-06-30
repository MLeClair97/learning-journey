# Battleship Game - Notes

## Date: June 30, 2025

## Process
- Learned a basic 5x5 board setup and randomint to set the battleship
- Added input validation for out-of-bounds guesses (numeric only - not alpha)
- Added a turn loop and guess checking logic
  
## What I Learned
- 2D lists and how to use them to represent a game board
- Conditional logic and nested if/else statements
- Input validation and error handling
- Looping through turns with "for" loops
- Basic debugging and print-based testing
  
## What I Struggled With
- Forgetting that "list.replace()" doesn't work for 2D lists - I started with that to capture the guesses - just needed to use "_board[guess_row][guess_col] = "X"_
- Accessing indices before checking bounds → got "IndexError"
    I was using the guess update above before checking if the number was greater than the board location
- Indentation and control flow nesting

## How I Solved It
- Rewrote nested conditions to check the entries were within the bounds *before* accessing / updating the guess list
- Asked ChatGPT for help understanding the logic flow and for help correcting indentations
  
