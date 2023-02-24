
def checkered_board(n):
    dark = '\u25A0'
    light = '\u25A1'
    board = ''
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                board += dark
            else:
                board += light
            if j != n-1:
                board += ' '
        if i != n-1:
            board += '\n'
    if n % 2 == 0:
        board = board.replace(dark, 'temp').replace(
            light, dark).replace('temp', light)
    return board


print(checkered_board(3))
