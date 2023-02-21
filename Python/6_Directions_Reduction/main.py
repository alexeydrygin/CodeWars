def dirReduc(arr):
    opposites = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    result = []
    for direction in arr:
        if result and opposites[direction] == result[-1]:
            result.pop()
        else:
            result.append(direction)
    return result
