# 5 Kyu - Find Out the Number of Gold Coins!

def number_of_coins(info):
    # Calculate the product of all moduli
    m = 1
    for _, mod in info:
        m *= mod

    # Calculate the sum of all residues
    x = 0
    for a, mod in info:
        b = m // mod
        x += a * b * pow(b, -1, mod)

    return x % m