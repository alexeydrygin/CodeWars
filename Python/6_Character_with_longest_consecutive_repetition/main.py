def longest_repetition(s):
    if not s:
        return ('', 0)

    curr_char = s[0]
    curr_count = 1
    max_char = curr_char
    max_count = curr_count

    for i in range(1, len(s)):
        if s[i] == curr_char:
            curr_count += 1
        else:
            if curr_count > max_count:
                max_char = curr_char
                max_count = curr_count
            curr_char = s[i]
            curr_count = 1

    if curr_count > max_count:
        max_char = curr_char
        max_count = curr_count

    return (max_char, max_count)
