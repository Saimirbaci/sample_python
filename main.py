import random

# Display the board
def display_board(board):
    print("\n")
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("   |   |")
    print("\n")

# Check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check for a draw
def check_draw(board):
    return ' ' not in board

# Get the player move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move in range(9) and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Get the computer move
def computer_move(board, player):
    available_moves = [i for i, x in enumerate(board) if x == ' ']
    move = random.choice(available_moves)
    board[move] = player

# Main game loop
def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    while True:
        display_board(board)
        
        if current_player == 'X':
            player_move(board, current_player)
        else:
            computer_move(board, current_player)
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
