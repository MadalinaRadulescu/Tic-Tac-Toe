def get_random_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass


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