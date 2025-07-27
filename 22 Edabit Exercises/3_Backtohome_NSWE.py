


coord_arr = [0,0]



# get user input

def backToHome(my_char):

    counter = {'N': 0, 'S':0, 'E': 0, 'W': 0}
    for char in my_char:
        counter[char] += 1

    final_pos = counter['N'] - counter['S'], counter['W'] - counter['E']

    if final_pos[0] + final_pos[1] != 0:
        return False
    else:
        return True
    

print( backToHome("EEWE") )
print( backToHome("NENESSWW")  )
print( backToHome("NEESSW") )
print()



print(backToHome("NNNN"))
print(backToHome("NENESSWW"))
print(backToHome("NEESSW"))
print(backToHome("EEWE"))
print(backToHome("NNSSEEEWWWEW"))
print(backToHome("NNNNWW"))