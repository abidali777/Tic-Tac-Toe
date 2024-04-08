def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter row number (0, 1, 2) for player {}: ".format(player)))
        col = int(input("Enter column number (0, 1, 2) for player {}: ".format(player)))
        
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("Player {} wins!".format(player))
                break
            player = "O" if player == "X" else "X"
        else:
            print("That position is already taken. Try again.")

tic_tac_toe()