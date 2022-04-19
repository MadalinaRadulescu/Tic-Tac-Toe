# human vs human 

def get_empty_board():
    emptyBoard = [[".", ".", "."],
                  [".", ".", "."],
                  [".", ".", "."]]
    return emptyBoard

def display_board(board):
    print()
    print("    1   2   3")
    print("A   " + board[0][0] + " | " + board[0][1]+ " | " + board[0][2])
    print("   ---+---+---")
    print("B   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("C   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()


def check_row(board):
  winner = None
  if board[0][0] == board[0][1] == board[0][2] and board[0][0] != ".":
    winner = board[0][0]
    
  elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != ".":
    winner = board[1][0]
   
  elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != ".":
    winner = board[2][0]

  return winner

def check_col(board):
  winner = None
  if board[0][0] == board[1][0] == board[2][0] and board[0][0] != ".":
    winner = board[0][0]
    
  elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != ".":
    winner = board[0][1]
    
  elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != ".":
    winner = board[0][2]
    
  return winner

def check_diag(board):
  winner = None
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ".":
    winner = board[0][0]
  elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != ".":
    winner = board[0][2]
  return winner

def get_winning_player(board):
  winner = check_row(board)
  if winner != None:
    return winner
  winner = check_col(board)
  if winner != None:
    return winner
  winner = check_diag(board)
  if winner != None:
    return winner

def get_human_coordinates(board, current_player):
    while True:
        user_input = input("Please enter a position: ")
        if user_input.upper() == "QUIT":
            print("Nice Game! See you next time.")
            quit()
        elif user_input.upper() == "A1":
            if board[0][0] == "X" or board[0][0] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((0, 0))
        elif user_input.upper() == "A2":
            if board[0][1] == "X" or board[0][1] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((0, 1))
        elif user_input.upper() == "A3":
            if board[0][2] == "X" or board[0][2] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((0, 2))
        elif user_input.upper() == "B1":
            if board[1][0] == "X" or board[1][0] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((1, 0))
        elif user_input.upper() == "B2":
            if board[1][1] == "X" or board[1][1] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((1, 1))
        elif user_input.upper() == "B3":
            if board[1][2] == "X" or board[1][2] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((1, 2))
        elif user_input.upper() == "C1":
            if board[2][0] == "X" or board[2][0] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((2, 0))
        elif user_input.upper() == "C2":
            if board[2][1] == "X" or board[2][1] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((2, 1))
        elif user_input.upper() == "C3":
            if board[2][2] == "X" or board[2][2] == "O":
                print("Position already taken. Try again.\n")
            else:
                return tuple((2, 2))
        else:
            print("Invalid input. Try again.\n")

def switchPlayer(current_player):
    if current_player == "X":
        current_player = "O"
        return current_player
    else:
        current_player = "X"
        return current_player

def is_board_full(board):
    if board[0].count(".") >= 1 or board[1].count(".") >= 1 or board[2].count(".") >= 1:
        return False
    else:
        return True

def get_random_ai_coordinates(board, current_player):
    import random
    coordinate = []
    numarLinie = 0
    for linie in board:
        numarColoana = 0
        for coloana in linie:
            if coloana == ".":
                coordinate.append(tuple((numarLinie, numarColoana)))

        numarColoana = numarColoana + 1
    numarLinie = numarLinie + 1

    if len(coordinate):
        return random.choice(coordinate)
    else:
        return None

def get_menu_option():
    print("Game options:\n1. Human vs Human\n2. Random AI vs Random AI\n3. Human vs Random AI\n4. Human vs Unbeatable AI")
    while True:
        opt_input = int(input("Select game mode: "))
        if opt_input < 5 and opt_input > 0:
            return opt_input
        else:
            print("Invalid input. Try Again.")

def main():
    board = get_empty_board()
    is_game_running = True
    current_player = "X"
    while is_game_running:
        display_board(board)
        x, y = get_human_coordinates(board, current_player)
        board[x][y] = current_player
        winner = get_winning_player(board)
        its_a_tie = is_board_full(board)
        if winner == "X" or winner == "O":
            display_board(board)
            print(f"The winner is Player {winner}!")
            break
        elif its_a_tie:
            display_board(board)
            print("It's a tie!")
            break
        current_player = switchPlayer(current_player)
        

if __name__ == "__main__":
    main()