# Hangman Game

A simple text-based Hangman game implemented in Python. Guess the word one letter at a time, and try to complete it before you run out of chances!

## Objective:
The goal is to guess the hidden word correctly by guessing one letter at a time.

## Rules:

You will be given a random word, and its letters will be hidden as underscores (_).
Guess one letter at a time. If the letter is correct, it will be revealed in the word.
If the letter is incorrect, your chances will decrease by one.
You win if you reveal the entire word before running out of chances.
You lose if you run out of chances without guessing the word.
Hints: The word is always the name of a fruit or vegetable.
Play Again: After completing a game, you will be prompted to play again. Enter yes to replay or no to exit.

## Features

Randomly selects a word from a predefined list of fruits and vegetables.
Provides hints and feedback for each guess.
Tracks and displays the guessed letters.
Allows the user to play multiple rounds until they choose to exit.

## Requirements

Python 3.6 or later

## Code Overview

Modules Used:
random: For selecting a random word.
collections.Counter: To track the guessed letters and their counts.

Main Components
play_hangman_game Function:
Encapsulates the game logic.

Handles user input validation, updates game state, and checks win/lose conditions.

Replay Option:
After each game, users can decide whether to play again or exit.

## How to Run

Clone the repository or copy the code into a Python file (e.g., hangman.py).
Run the script in your terminal or Python IDE:
python hangman.py

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback is valuable!

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code as per the license terms.

## Author

Created with ❤️ by Dhatsheth Roshan.

