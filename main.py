# function building 

def game_board(): 

    game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    
    # just putting the game board of the game 

    print("   0  1  2") # status 
     
    for count, row in enumerate(game):
        print(count, row)

    game[0][1] = 2 # now we are assigning
    
    # what if we did a random sequence of numbers into the list arrays 
    print("   0  1  2") # status 
    for count, row in enumerate(game):
        print(count, row)

