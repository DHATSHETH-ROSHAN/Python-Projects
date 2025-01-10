# Number Guessing Game

Welcome to the **Number Guessing Game**! In this game, the program will randomly select a number between a user-defined lower and upper bound, and you need to guess the number within a limited number of attempts.

The game provides hints and visual feedback on your progress using a progress bar. The goal is to guess the number within the allowed attempts. If you don't succeed, you can try again by restarting the game.

## Features:
- The game selects a random number between a lower and upper bound specified by the user.
- The number of chances (attempts) to guess the correct number is calculated using the logarithmic formula.
- A progress bar shows your progress as you guess the number, with a fun representation using symbols.
- The game provides a hint (whether the number is odd or even) when you've used the second chance.
- The user can choose to play again or exit after each round.

## How to Play:
1. **Enter the bounds**: When the game starts, you'll be asked to input a lower and an upper bound to define the range for the random number.
2. **Guess the number**: Try to guess the number within the given chances.
3. **Hints**: After two attempts, a hint will be provided telling you whether the number is odd or even.
4. **Feedback**: After each guess, the game will tell you if your guess was too high, too low, or correct.
5. **Play Again**: Once you've either guessed the number correctly or run out of attempts, you can choose to play again.

## Installation:
To run this game on your local machine, make sure you have Python installed.

1. Clone the repository to your local machine:
   ```bash
   git clone git clone https://github.com/DHATSHETH-ROSHAN/Python-Projects/basic/number-guessing-game.git


## Requirements
- Python 3.x
- tqdm library (for the progress bar)

## Code Explanation:
chance(lb, ub): This function calculates the number of chances based on the difference between the upper and lower bounds, using a logarithmic formula.
progress_bar(guess, chances): This function visualizes the progress using a bar with symbols, representing how many attempts you've used.
Gameplay Flow: The user inputs the lower and upper bounds, and the game starts. The user guesses a number within a limited number of chances. Hints and feedback are provided to help the user make a correct guess.

## Dependencies:
No external libraries are required for this project. It uses only built-in Python libraries:
random
math

## Contributing:
Feel free to fork this repository and submit a pull request with your changes. If you want to add new features or improvements, don't hesitate to contribute.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.
