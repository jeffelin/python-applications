# function

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def addition(x,y): 
    return x+y 


def game_board_v1(): 

    game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)


def game_board_v2(current_game, player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game): 
        print(count, row) 
    return current_game


def check_winner_of_game(current_game_board): 
    # horizontal rows 
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0: 
            print(f"Player {row[0]} is the Winner by Horizontal Destruction!")
    
    # vertical columns 
    for column in range(len(game[0])):
        vertical_column = [] 
        for row in game:
            vertical_column.append(row[column])
            if vertical_column.count(row[0]) == len(row) and row[0] != 0: 
                print(f"Player {row[0]} is the Winner by Vertical Destruction!")

    # / diagonal
    right_diagonals = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        right_diagonals.append(game[idx][reverse_idx])

    if right_diagonals.count(right_diagonals[0]) == len(right_diagonals) and right_diagonals[0] != 0:
        print(f"Player {right_diagonals[0]} has won Diagonally to the RIGHT!")

    # \ diagonal
    left_diagonals = []
    for ix in range(len(game)):
        left_diagonals.append(game[ix][ix])

    if left_diagonals.count(left_diagonals[0]) == len(left_diagonals) and left_diagonals[0] != 0:
        print(f"Player {left_diagonals[0]} has won Diagonally to the LEFT!")

def final_game_board(game_map, player=0, row=0, column=0, just_display=False): 

    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False

def new_size(game_size): 
    game_size = 5

    game = []
    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        game.append(row)

    print(game)

# ---------------------------------------------------


# # dump:
#     # print("   0  1  2")
    # if not just_display:
    #     game[row][column] = player
    # for count, row in enumerate(game):
    #     print(count, row)

    # game[0][1] = 2 # now we are assigning
    
    # # what if we did a random sequence of numbers into the list arrays 
    # print("   0  1  2") # status 
    # for count, row in enumerate(game):
    #     print(count, row)
