import random

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
  """
  Should return the player that wins based on the tic tac toe rules.
  If no player has won, than "None" is returned.
  """
  winner = check_row(board)
  if winner != None:
    return winner
  winner = check_col(board)
  if winner != None:
    return winner
  winner = check_diag(board)
  if winner != None:
    return winner

board = [
    ["X", "O", "."],
    ["O", "X", "."],
    ["X", "X", "O"],
  ]
  
def get_random_ai_coordinates(board):
    coordinate = []
    numarLinie = 0
    for linie in board:
        numarColoana = 0
        for coloana in linie:
            if coloana == ".":
                coordinate.append(tuple((numarLinie, numarColoana)))
                numarColoana = numarColoana + 1
            else:
                numarColoana = numarColoana + 1
        numarLinie = numarLinie + 1
    move = 0
    for let in ["O", "X"]:
        for (x, y) in coordinate:
            boardCopy = board.copy()
            boardCopy[x][y] = let
            if get_winning_player(boardCopy):
                move = (x, y)
                return move
    cornersOpen = []
    for (x, y) in coordinate:
        if (x, y) in [(0, 0), (0, 2), (2, 2), (2, 0)]:
            cornersOpen.append((x, y))
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if (1, 1) in coordinate:
        move = (1, 1)
        return move
    
    edgesOpen = []
    for (x, y) in coordinate:
        if (x, y) in [(0, 1), (1, 2), (2, 1), (1, 0)]:
            edgesOpen.append((x, y))
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(list):
    if len(list) > 0:
        return random.choice(list)
    else:
        return None

print(get_random_ai_coordinates(board))
