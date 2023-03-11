# 7 Kyu - Find the next perfect square

import math

def find_next_square(sq):
    # If the square root of sq is an integer, find the next square
    if math.sqrt(sq).is_integer():
        return int(math.pow(math.sqrt(sq) + 1, 2))
    else:
        return -1