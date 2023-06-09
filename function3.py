from function0 import display_board


def get_human_coordinates(board, current_player):
  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """
  while True:
    user_input = input("\nPlease enter a position: ")
    if user_input.upper() == "QUIT":
      print("\nNice Game! See you next time.\n")
      quit()
    elif user_input.upper() == "A1":
      if board[0][0] != ".": #or board[0][0] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((0, 0))
    elif user_input.upper() == "A2":
      if board[0][1] != ".": # or board[0][1] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((0, 1))
    elif user_input.upper() == "A3":
      if board[0][2] != ".": # or board[0][2] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((0, 2))
    elif user_input.upper() == "B1":
      if board[1][0] != ".": # or board[1][0] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((1, 0))
    elif user_input.upper() == "B2":
      if board[1][1] != ".": # or board[1][1] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((1, 1))
    elif user_input.upper() == "B3":
      if board[1][2] != ".": # or board[1][2] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((1, 2))
    elif user_input.upper() == "C1":
      if board[2][0] != ".": # or board[2][0] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((2, 0))
    elif user_input.upper() == "C2":
      if board[2][1] != ".": # or board[2][1] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((2, 1))
    elif user_input.upper() == "C3":
      if board[2][2] != ".": # or board[2][2] == "O":
          print("\nPosition already taken. Try again.")
      else:
          return tuple((2, 2))
    else:
      print("\nInvalid input. Try again.")
        


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones