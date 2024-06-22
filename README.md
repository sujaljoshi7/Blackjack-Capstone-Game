# Blackjack Capstone Game

Welcome to the Blackjack Capstone Game! This is a simple implementation of the classic card game Blackjack using Python.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Contributing](#contributing)

## Introduction

Blackjack, also known as 21, is a popular card game where the goal is to have a hand value as close to 21 as possible
without going over. This implementation allows you to play against the computer.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/sujaljoshi7/Blackjack-Capstone-Game.git
    ```

2. **Ensure you have Python installed:**

   This script requires Python 3.x. You can download it from [python.org](https://www.python.org/).

3. **Ensure you have the `art` file in the same directory:**

   Make sure the `art.py` file containing the logo is in the same directory as the main script.

## How to Play

1. **Run the Program:**

   To start the program, simply run the Python script:


2. **Gameplay:**

    - The game will print the logo and ask if you want to play a game of Blackjack.
    - You will be dealt two cards and the computer will be dealt two cards.
    - Your goal is to get as close to 21 as possible without going over.
    - You can choose to draw another card or pass.
    - The computer will keep drawing cards until it reaches a score of at least 17.
    - The winner is determined based on the final scores of both hands.

3. **Example:**

    ```bash
    Do you want to play a game of Blackjack? Type 'y' or 'n': y
    Your cards: [10, 9], current score: 19
    Computer's first card: 6
    Type 'y' to get another card, type 'n' to pass: n
    Your final hand: [10, 9], final score: 19
    Computer's final hand: [6, 10, 2], final score: 18
    You win 😃
    ```

## Features

- Simple implementation of Blackjack.
- Allows continuous play.
- Clear and concise text-based interface.
- Handles special conditions like Blackjack and going over 21.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---

**Note:** Ensure you have the `art.py` file in the same directory as the main script to display the logo. This script
does not use any other external modules beyond the Python standard library.
