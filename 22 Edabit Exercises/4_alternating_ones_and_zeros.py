
def can_alternate(s):

    el1 = 0
    el2 = 0

    for elem in s:
        if elem == '0': el1 += 1
        else:           el2 += 1

    if abs( el1 - el2 ) <= 1:
        return True
    
    return False


print( can_alternate("0001111") )
print( can_alternate("01001") )
print( can_alternate("010001") )
print( can_alternate("1111") )