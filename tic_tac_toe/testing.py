# testing cases 

from main import game_board_v1
from main import game_board_v2
from main import check_winner_of_game

# initializing 

game_initial = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

game_test = [[0, 2, 1],
        [0, 2, 2],
        [1, 2, 1]]


game_board_v1()
game_board_v2(game_test)
