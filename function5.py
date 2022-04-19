import copy
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

def get_umbeatable_ai_coordinates(board, current_player):
  import copy
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  possibleMoves = []
  numarRow = 0
  for row in board:
    numarCol = 0
    for col in row:
      if col == ".":
        possibleMoves.append(tuple((numarRow, numarCol)))
        numarCol = numarCol + 1
      else:
        numarCol = numarCol + 1
    numarRow = numarRow + 1
  move = 0
  for let in ["O", "X"]:
    for (x, y) in possibleMoves:
      boardCopy = copy.deepcopy(board)
      boardCopy[x][y] = let
      if get_winning_player(boardCopy):
        move = (x, y)
        return move

  if (1, 1) in possibleMoves:
    move = (1, 1)
    return move

  cornersOpen = []
  for (x, y) in possibleMoves:
    if (x, y) in [(0, 0), (0, 2), (2, 2), (2, 0)]:
      cornersOpen.append((x, y))
      
  if len(cornersOpen) > 0:
    move = selectRandom(cornersOpen)
    return move

    
  edgesOpen = []
  for (x, y) in possibleMoves:
      if (x, y) in [(0, 1), (1, 2), (2, 1), (1, 0)]:
          edgesOpen.append((x, y))
  if len(edgesOpen) > 0:
    move = selectRandom(edgesOpen)
    return move

def selectRandom(list):
  import random
  if len(list) > 0:
      return random.choice(list)
  else:
      return None


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_umbeatable_ai_coordinates(board_1, "X")) # the printed coordinate should always be (0, 0)

  board_2 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print(get_umbeatable_ai_coordinates(board_2, "O")) # the printed coordinate should always be (1, 1)

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_umbeatable_ai_coordinates(board_3, "X")) # the printed coordinate should be either (0, 2) or (2, 0)