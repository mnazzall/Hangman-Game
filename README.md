# Hangman-Game

A classic text-based Hangman game built with Python. This project was developed as part of a Python programming internship to demonstrate core logic, control structures, and input validation.

## Features
* **Randomized Gameplay:** Selects a random word from a predefined tech-focused list (`developer`, `hardware`, `software`, `algorithm`, `coding`) for every new session.
* **Robust Input Validation:** Prevents crashes by ensuring players only enter single, alphabetical characters.
* **Attempt Tracking:** Keeps a real-time count of remaining lives (starts with 6) and displays the current state of the hidden word.
* **Duplicate Guess Handling:** Uses Python sets to remember previously guessed letters, prompting the user to try again without penalizing their attempt count.

## Prerequisites
* Python 3.x installed on your system.

## How to Play
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the script using the following command:
   ```bash
   python hangman.py
