import math
import os
os.system('cls')

def square_root(x):
    return math.sqrt(x)

list_square=[4,9,16,25,36,49]
list_squareroot=map(square_root, list_square)
print(list(list_squareroot))