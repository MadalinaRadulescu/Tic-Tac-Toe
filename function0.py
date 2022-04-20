def display_board(board):
  """
  Should print the tic tac toe board in a format similar to
       1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       --+---+---
    C   0 | X | . 
       --+---+---
  """
  print()
  print("    1   2   3")
  print("A   " + board[0][0] + " | " + board[0][1]+ " | " + board[0][2])
  print("   ---+---+---")
  print("B   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
  print("   ---+---+---")
  print("C   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
  print()
  



if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."]
    ]
    display_board(board)
    # should print 
    #     1   2   3
    # A   X | O | . 
    #    ---+---+---
    # B   X | O | .
    #    --+---+---
    # C   0 | X | . 
    #    --+---+---