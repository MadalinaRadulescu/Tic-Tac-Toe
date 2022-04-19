from function0 import display_board
from function1 import get_menu_option
from function2 import get_empty_board
from function3 import get_human_coordinates
from function4 import get_random_ai_coordinates
from function5 import get_umbeatable_ai_coordinates
from function6 import get_winning_player
from function7 import is_board_full
from function8 import switchPlayer

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():
    import time
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = 'X'
    while is_game_running:
        if game_mode == 1:
            display_board(board)
            x, y = get_human_coordinates(board, current_player)
            board[x][y] = current_player
            winner = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if winner == "X" or winner == "O":
                display_board(board)
                print(f"The winner is Player {winner}!")
                break
            elif its_a_tie:
                display_board(board)
                print("It's a tie!")
                break
            current_player = switchPlayer(current_player)
        elif game_mode == 2:
            display_board(board)
            x, y = get_random_ai_coordinates(board, current_player)
            board[x][y] = current_player
            time.sleep(1)
            winner = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if winner == "X" or winner == "O":
                display_board(board)
                print(f"The winner is Player {winner}!")
                break
            elif its_a_tie:
                display_board(board)
                print("It's a tie!")
                break
            current_player = switchPlayer(current_player)

        elif game_mode == 3:
            display_board(board)
            if current_player == "X":
                x, y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
            else:
                x,y = get_random_ai_coordinates(board, current_player)
                board[x][y] = current_player
            winner = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if winner == "X" or winner == "O":
                display_board(board)
                print(f"The winner is Player {winner}!")
                break
            elif its_a_tie:
                display_board(board)
                print("It's a tie!")
                break
            current_player = switchPlayer(current_player)
        elif game_mode == 4:
            display_board(board)
            if current_player == "X":
                x, y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
            else:
                x,y = get_umbeatable_ai_coordinates(board, current_player)
                board[x][y] = current_player
            winner = get_winning_player(board)
            its_a_tie = is_board_full(board)
            if winner == "X" or winner == "O":
                display_board(board)
                print(f"The winner is Player {winner}!")
                break
            elif its_a_tie:
                display_board(board)
                print("It's a tie!")
                break
            current_player = switchPlayer(current_player)
        
        


if __name__ == "__main__":
    main()