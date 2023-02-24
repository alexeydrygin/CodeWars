def number_of_pairs(gloves):
    colors = {}
    for glove in gloves:
        if glove in colors:
            colors[glove] += 1
        else:
            colors[glove] = 1
    pairs = 0
    for count in colors.values():
        pairs += count // 2
    return pairs
