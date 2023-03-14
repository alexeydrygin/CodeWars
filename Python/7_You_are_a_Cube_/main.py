# 7 kyu - You are a Cube!
def isPerfectCube(n):
    cubeRoot = round(n**(1/3))
    return cubeRoot**3 == n
