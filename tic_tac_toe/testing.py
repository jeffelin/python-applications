# testing cases 
import secrets 
# from main import game_board_v1
# from main import game_board_v2
from main import final_game_board
from main import check_winner_of_game

# initializing 

game_initial = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

game_test = [[0, 2, 1],
        [0, 2, 2],
        [1, 2, 1]]


play = True 
players = [1,2]
while play: 
    game_initial 


game_won = False 
current_player = secrets.choice(players)

game = final_game_board(game_initial, player =1, row =3, column =1)