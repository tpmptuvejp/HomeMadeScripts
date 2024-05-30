print('Tic-Tac-Toe, Game by SoloStudio')                                
print('---------')
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ['X', 'O']
        current_player = 0
        moves_left = 9

        while moves_left > 0:
            print_board(board)
            player = players[current_player]
            print(f"Player {player}'s turn")
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1

            if board[row][col] == " ":
                board[row][col] = player
                moves_left -= 1
                if check_winner(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                current_player = (current_player + 1) % 2
            else:
                print("That position is already taken. Try somewhere else.")

        if moves_left == 0:
            print_board(board)
            print("It's a tie!")

        if not restart_game():
            print ('Thanks for playing.')
            break

def restart_game():
    return input("Do you want to play again? (y/n): ").lower() == 'y'
tic_tac_toe()

#SoloStudio-2024
