# Hangman Game

Welcome to the **Hangman Game**! This is a text-based word-guessing game where the objective is to guess the hidden word one letter at a time before you run out of chances. The words are chosen randomly and are names of fruits or vegetables.

## Features:
- Randomly selects a word from a predefined list of fruits and vegetables.
- Provides hints to help identify the word.
- Tracks and displays the guessed letters.
- Allows users to play multiple rounds until they decide to quit.
- Displays the full word and a win/lose message at the end of each game.

## How to Play:
1. **Start the Game**: When the game begins, a word is selected randomly, and its letters are hidden as underscores (`_`).
2. **Guess Letters**: Enter one letter at a time to guess the word.
   - Correct guesses reveal the corresponding letters in the word.
   - Incorrect guesses reduce your remaining chances.
3. **Hints**: The game provides a hint that the word is the name of a fruit or vegetable.
4. **Win/Lose**: You win if you guess all the letters correctly before running out of chances. If you fail, the full word will be revealed.
5. **Play Again**: After each round, choose whether to play again or exit the game.

## Installation:
To run this game on your local machine, ensure you have Python installed.

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/DHATSHETH-ROSHAN/Python-Projects/basic/hangman-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```
3. Run the game:
   ```bash
   python hangman.py
   ```

## Requirements:
- Python 3.x

## Code Explanation:
- **play_hangman_game**: This function contains the main game logic, including input validation, tracking guessed letters, and checking win/lose conditions.
- **Replay Option**: After each game, the user can choose to play another round or exit.

## Dependencies:
No external libraries are required for this project. It uses only built-in Python libraries:
- **random**: For selecting a random word.
- **collections.Counter**: To track and count guessed letters.

## Contributing:
Feel free to fork this repository and submit a pull request with your changes. If you want to add new features or improvements, don't hesitate to contribute.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.

