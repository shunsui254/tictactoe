# Tic Tac Toe Terminal Game

## Overview

This repository contains a Python implementation of the classic Tic Tac Toe game designed to be played in the terminal. The project features two main classes: `TicTacToe`, which handles the core game logic and board management, and `Game`, which manages user interactions, player information, scoring, and the overall game flow. It’s a perfect project to explore game logic in Python while enjoying a timeless board game with friends.

## Features

- **Interactive Board Display:**  
  Shows both the current game state and a numbered board guide to help players choose their moves.

- **Player Management:**  
  Players input their names and select symbols (X or O). The game automatically assigns the opposing symbol and manages turn sequences.

- **Move Validation:**  
  Ensures that moves are within the correct range and that players do not overwrite occupied positions.

- **Win, Tie & Unwinnable Checks:**  
  The game continuously checks for winning conditions across rows, columns, and diagonals. It also detects tie situations or states where no winning move exists, gracefully ending the round.

- **Leaderboard:**  
  Tracks wins across rounds, allowing players to see their scores and engage in multiple rounds with a cumulative leaderboard.

- **User-Friendly Terminal UI:**  
  The intuitive CLI guides players from the main menu through each round, making the experience as engaging as it is easy to play.

## Getting Started

### Prerequisites

- **Python 3.6 or Higher:**  
  Ensure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/).

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/shunsui254/tic-tac-toe.git

2. **Navigate to the Project Directory:**

   ```bash
   cd tic-tac-toe
(This project uses Python’s standard library, so no external dependencies are required.)

## Running the Game

**Launch the game by running the following command in your terminal:**

     python tic_tac_toe.py

You will be greeted with a main menu where you can choose to start a game or quit.

## How to Play
Starting a Game: At the main menu, type play to begin a new game session.

Entering Player Information: Input the names of the two players and have the first player choose their symbol (either X or O). The game will automatically set the second player's symbol.

Understanding the Board: The game will first display a numbered board, helping players understand which number corresponds to which board position.

Making a Move: On your turn, enter the position number (1-9) where you would like to place your symbol. The game validates your move and prompts for re-entry if the move is invalid.

Determining the Outcome: After each move, the game checks for a win condition (three in a row), a tie (board full), or an unwinnable state (no possible win combinations remain). A congratulatory message is shown if you win, and the appropriate message is shown if it’s a draw.

Continuing Play: After a round finishes, the leaderboard is updated with current scores. You can choose whether to play another round or exit to the main menu. 

## Code Structure

    TicTacToe Class:
    
    __init__: Initializes the game board and sets the default starting player.
    
    print_board & print_board_nums: Display functions for both the current game state and a guide board with numeric positions.
    
    available_moves: Lists all available moves based on empty board positions.
    
    make_move: Applies the current player's move to the board.
    
    switch_player: Alternates the active player at the end of each move.
    
    check_winner: Checks rows, columns, and diagonals for a winning move.
    
    is_tie & is_unwinnable: Detect drawing conditions and scenarios in which reaching a win is no longer possible.
    
    Game Class:
    
    main_menu: Provides the initial menu for playing or quitting.
    
    start_game: Sets up game rounds, managing user inputs, validating moves, and updating the leaderboard.
    
    get_player_info: Collects and assigns player names and symbols.
    
    get_valid_position: Ensures players select valid board positions.
    
    display_leaderboard & ask_to_play_again: Manage post-game interactions and round restarts.

### Contributing
We welcome contributions! If you have suggestions for improvements or new features, please feel free to fork the repository and submit a pull request. You can also open an issue if you encounter any bugs or have ideas to enhance the gameplay experience.

### License
This project is licensed under the MIT License.

## Acknowledgments
Inspired by classic board games and built as a learning project, this Tic Tac Toe game is a fun exercise in managing game logic with Python. Enjoy playing, and feel free to explore or expand the code to customize your game experience!

Happy gaming!

    ---
    Let me know if you'd like any further changes or additions to this file!


