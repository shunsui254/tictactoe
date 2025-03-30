class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 board
        self.current_player = "X"

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # Shows which number corresponds to which position
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position):
        self.board[position] = self.current_player

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            if all(spot == row[0] and spot != " " for spot in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[col+i*3] == self.current_player and self.board[col+i*3] != " " for i in range(3)):
                return True

        # Check diagonals
        diagonals = [[0, 4, 8], [2, 4, 6]]
        for diagonal in diagonals:
            if all(self.board[i] == self.current_player and self.board[i] != " " for i in diagonal):
                return True

        return False

    def is_tie(self):
        return " " not in self.board

    def is_unwinnable(self):
        # Check if any winning combination is still achievable
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            values = [self.board[i] for i in combo]
            if values.count("X") > 0 and values.count("O") > 0:
                continue  # Both players occupy this combination, so it's blocked
            if values.count(" ") > 0:
                return False  # At least one combination is still achievable
        return True  # No winning combinations are left


class Game:
    def __init__(self):
        self.scores = {}
        self.player1_name = ""
        self.player2_name = ""
        self.player1_symbol = ""
        self.player2_symbol = ""

    def main_menu(self):
        while True:
            print("\nWelcome to Tic Tac Toe!")
            menu_choice = input("Would you like to play or quit? (play/quit): ").strip().lower()
            if menu_choice == "play":
                print("\nStarting a new game...\n")
                self.start_game()
            elif menu_choice == "quit":
                print("Thank you for playing! Goodbye!")
                return
            else:
                print("Invalid input! Please type 'play' or 'quit'.")

    def start_game(self):
        self.get_player_info()
        while True:
            game = TicTacToe()
            game.current_player = self.player1_symbol  # Start with Player 1
            print("\nHere are the position numbers:")
            game.print_board_nums()

            while True:
                print(f"\nCurrent player: {self.get_current_player_name(game.current_player)}")
                game.print_board()

                position = self.get_valid_position(game)
                game.make_move(position)

                if game.check_winner():
                    winner = self.get_current_player_name(game.current_player)
                    print(f"\nPlayer {winner} wins!")
                    game.print_board()
                    print(f"Congratulations {winner}! Thank you for playing!")
                    self.scores[winner] += 1
                    break

                if game.is_tie() or game.is_unwinnable():
                    print("\nIt's a draw!")
                    game.print_board()
                    print("Thank you for playing!")
                    break

                game.switch_player()

            self.display_leaderboard()
            if not self.ask_to_play_again():
                return

    def get_player_info(self):
        self.player1_name = input("Player 1 Name? ").strip()
        self.player2_name = input("Player 2 Name? ").strip()

        while True:
            self.player1_symbol = input(f"{self.player1_name}, do you want to play as X or O? ").strip().upper()
            if self.player1_symbol in ["X", "O"]:
                break
            print("Invalid input! Please choose X or O.")

        self.player2_symbol = "O" if self.player1_symbol == "X" else "X"
        print(f"{self.player1_name} will play as {self.player1_symbol}, and {self.player2_name} will play as {self.player2_symbol}.")
        self.scores = {self.player1_name: 0, self.player2_name: 0}

    def get_current_player_name(self, symbol):
        return self.player1_name if symbol == self.player1_symbol else self.player2_name

    def get_valid_position(self, game):
        while True:
            try:
                position = int(input("Enter position (1-9): ")) - 1  # Adjust input to zero-based index
                if position in game.available_moves():
                    return position
                print("Invalid move! The position is already taken or out of range. Try again.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")

    def display_leaderboard(self):
        print("\nLeaderboard:")
        for player, score in self.scores.items():
            print(f"{player}: {score} wins")

    def ask_to_play_again(self):
        while True:
            choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if choice == "yes":
                print("\nStarting a new game...\n")
                return True
            elif choice == "no":
                print("Thank you for playing! Returning to the main menu...")
                return False
            else:
                print("Invalid input! Please type 'yes' or 'no'.")


if __name__ == "__main__":
    game = Game()
    game.main_menu()