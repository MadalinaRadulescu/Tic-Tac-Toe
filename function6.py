

from importlib.machinery import WindowsRegistryFinder


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
  


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_winning_player(board_1)) # should return "X"

  board_2 = [
    ["X", "O", "O"],
    ["X", "O", "."],
    ["O", "X", "X"],
  ]
  print(get_winning_player(board_2)) # should return "O"

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_winning_player(board_3)) # should return None