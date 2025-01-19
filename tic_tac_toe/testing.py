# testing cases 
import secrets 
import itertools
# from main import game_board_v1
# from main import game_board_v2
from main import final_game_board
from main import check_winner_of_game


# play 

game_test = [] 

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    player_cycle = itertools.cycle([1, 2])
    final_game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Player: {current_player}")
            column_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = final_game_board(game, player=current_player, row=row_choice, column=column_choice)

        if check_winner_of_game(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting!")
            elif again.lower() == "n":
                print("Byeeeee!!!")
                play = False
            else:
                print("Not a valid answer, but... c ya!")
                play = False

# testing

# game = final_game_board(game_initial, player =1, row =2, column =1)