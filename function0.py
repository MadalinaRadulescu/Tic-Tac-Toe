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
  pass



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