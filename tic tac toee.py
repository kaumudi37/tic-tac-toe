def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def get_player_move(player):
    while True:
        try:
            row = int(input(f"{player}, enter row (1-3): ")) - 1
            col = int(input(f"{player}, enter column (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_tic_tac_toe():
    print("Welcome to Tic Tac Toe!")

    players = int(input("How many players? (1 or 2): "))

    if players not in [1, 2]:
        print("Invalid number of players. Exiting.")
        return

    player_names = []
    for i in range(players):
        player_name = input(f"Enter name for Player {i + 1}: ")
        player_names.append(player_name)

    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    current_player_index = 0

    while True:
        print_board(board)

        current_player = player_names[current_player_index]
        row, col = get_player_move(current_player)

        board[row][col] = 'X' if current_player_index == 0 else 'O'

        if check_winner(board):
            print_board(board)
            print(f"{current_player} wins! Congratulations!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie! The board is full.")
            break

        current_player_index = 1 - current_player_index  # Switch player


if __name__ == "__main__":
    play_tic_tac_toe()
