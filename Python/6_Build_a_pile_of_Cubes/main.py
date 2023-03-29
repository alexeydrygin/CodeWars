# 6 kyu - Build a pile of Cubes
def find_nb(m):
    n = 1
    sum_of_cubes = 1
    while sum_of_cubes < m:
        n += 1
        sum_of_cubes += n ** 3
    if sum_of_cubes == m:
        return n
    else:
        return -1
