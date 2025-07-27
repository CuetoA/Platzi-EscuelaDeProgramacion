'''
This challenge is based on the classic videogame "Snake".

Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.

For example, if n = 7 the game looks something like this:



In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).

Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs out of space in the game screen.

Examples
snakefill(3) ➞ 3

snakefill(6) ➞ 5

snakefill(24) ➞ 9
Notes
The given number will always be a positive integer (there are no exceptions to handle).
'''

import math 

# Brute force
def snakefill(n):
    space = n * n

    length = 1
    counter = -1
    while length < space:
        length *= 2
        counter += 1
    
    return counter

# Stratey
def snakefill2(n):
    return math.floor( 2 * math.log(n) / math.log(2) ) 

print( snakefill(3) )
print( snakefill(6) )
print( snakefill(24) )
print( snakefill(8) )
print( snakefill(18) )
print( snakefill(555) )
print( snakefill(2) )
print( snakefill(1) )
print( snakefill(900) )
print()
print( snakefill2(3) )
print( snakefill2(6) )
print( snakefill2(24) )
print( snakefill2(8) )
print( snakefill2(18) )
print( snakefill2(555) )
print( snakefill2(2) )
print( snakefill2(1) )
print( snakefill2(900) )