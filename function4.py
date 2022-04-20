
from function6 import get_winning_player
import copy

def get_random_ai_coordinates(board, current_player):
  import random
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
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

    numarRow = numarRow + 1

  move = 0
  for let in ["O", "X"]:
    for (x, y) in possibleMoves:
      boardCopy = copy.deepcopy(board)
      boardCopy[x][y] = let
      if get_winning_player(boardCopy):
        move = (x, y)
        return move
    
  cornersOpen = []
  for (x, y) in possibleMoves:
    if (x, y) in [(0, 0), (0, 2), (2, 2), (2, 0)]:
      cornersOpen.append((x, y))
      
  if len(cornersOpen) > 0:
    move = selectRandom(cornersOpen)
    return move

  if (1, 1) in possibleMoves:
    move = (1, 1)
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
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)

  board_2 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print(get_random_ai_coordinates(board_2, "O")) # the printed coordinate should be None