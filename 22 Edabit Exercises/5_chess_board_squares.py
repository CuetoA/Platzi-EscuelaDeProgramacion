

def chess_board(pole):
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    
    #split array
    c1, c2 = dict[ pole[0]] , int(pole[1])
    
    #If even -> black
    if (c1 + c2) % 2 == 0:  return "black"
    else:                   return "white"


print( chess_board("a1") )
print( chess_board("e5") )
print( chess_board("d1") )