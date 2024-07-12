def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {players[current_player]}, enter the column (0, 1, 2): "))

        if board[row][col] != ' ':
            print("Cell already taken! Try again.")
            continue

        board[row][col] = players[current_player]

        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 1 - current_player


tic_tac_toe()
