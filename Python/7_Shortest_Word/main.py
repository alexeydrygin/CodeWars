def find_short(s):
    words = s.split()
    shortest_length = len(words[0])
    for word in words[1:]:
        if len(word) < shortest_length:
            shortest_length = len(word)
    return shortest_length