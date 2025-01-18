# testing cases 

from main import game_board_v1
from main import game_board_v2
from main import check_winner_of_game

# initializing 

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


# run with game 

game_board_v2(game) 
game_board_v2(game, player=2, row=0, column=0)
