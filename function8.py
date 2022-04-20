def switchPlayer(current_player):
    if current_player == "X":
        current_player = "O"
        return current_player 
    else:
        current_player = "X"
        return current_player