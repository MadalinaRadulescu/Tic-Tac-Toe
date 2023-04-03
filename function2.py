def get_empty_board():
    '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    '''
    # emptyBoard = [[".", ".", "."],
    #               [".", ".", "."],
    #               [".", ".", "."]]
    emptyBoard = []
    for n in range(9):
        i = []
        for m in range(3):
            j = "."
            i.append(j)
        emptyBoard.append(i)
        

    return emptyBoard

if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = get_empty_board()
    print(board)
