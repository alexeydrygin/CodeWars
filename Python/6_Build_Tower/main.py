# 6 kyu - Build Tower
def tower_builder(n):
    tower = []
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        tower.append(spaces + stars + spaces)
    return tower
