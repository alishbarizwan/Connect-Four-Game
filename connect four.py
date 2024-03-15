                                                                             # Connect Four Game

# Constants
ROWS = 6
COLUMNS = 7

# empty game board
board = []
for i in range(ROWS):
    row = []
    for j in range(COLUMNS):
        row.append(' ')
    board.append(row)

def print_board():
    """current state of the game board"""
    for row in board:
        print('|'.join(row))

def drop_piece(column, symbol):

    for i in range(ROWS-1, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = symbol
            return

def is_winner(symbol):
    """checking winner"""
    # Check for horizontal win
    for row in board:
        for i in range(COLUMNS-3):
            if row[i] == symbol and row[i+1] == symbol and row[i+2] == symbol and row[i+3] ==symbol:
                return True
    # Check for vertical win
    for j in range(COLUMNS):
        for i in range(ROWS-3):
            if board[i][j] == symbol and board[i+1][j] == symbol and board[i + 2][j] == symbol and board[i + 3][j] == symbol:
                return True
    # Check for diagonal win
    for i in range(ROWS-3):
        for j in range(COLUMNS-3):
            if board[i][j] == symbol and board[i + 1][j + 1] == symbol and board[i + 2][j + 2] == symbol and board[i + 3][j + 3] == symbol:
                return True
    for i in range(ROWS-3):
        for j in range(COLUMNS-3):
            if board[i][j+3] == symbol and board[i + 1][j + 2] == symbol and board[i + 2][j + 1] == symbol and board[i + 3][j] == symbol:
                return True
    return False

# Game loop
player1 = input("PLAYER 1:Enter your name: ")
player2=input("PLAYER 2:Enter your name ")
player=player1
while True:
    print_board()
    try:
        column = int(input(f'{player}, choose a column: '))
        if column>=7:
            print(f"\n{player}! You have entered wrong value\nTry again!")
            continue
        if player==player1:
            drop_piece(column,"X")
            if is_winner("X"):
                print_board()
                print(f'{player} wins!')
                break
        else:
            drop_piece(column, "O")
            if is_winner("O"):
                print_board()
                print(f'{player} wins!')
                break
        player = player2 if player == player1 else player1
    except:
        print(f"\n{player}! You have entered something wrong\nTry again!")