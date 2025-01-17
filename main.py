# function building 

def addition(x,y): 
    return x+y 


def game_board_v1(): 

    game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

    
    # just putting the game board of the game 

    print("   0  1  2") # status 
     
    for count, row in enumerate(game):
        print(count, row)

    # game[0][1] = 2 # now we are assigning
    
    # # what if we did a random sequence of numbers into the list arrays 
    # print("   0  1  2") # status 
    # for count, row in enumerate(game):
    #     print(count, row)

def game_board_v2(player, row, column): 
    
    game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    
    game[row][column] = player 
    print("   0  1  2") 
    
    for count, row in enumerate(game):
        print(count, row)


    # print("   0  1  2")
    # if not just_display:
    #     game[row][column] = player
    # for count, row in enumerate(game):
    #     print(count, row)
