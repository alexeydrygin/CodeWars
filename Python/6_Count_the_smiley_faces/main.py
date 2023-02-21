def count_smileys(arr):
    count = 0
    for face in arr:
        if len(face) == 2:
            if (face[0] == ':' or face[0] == ';') and (face[1] == ')' or face[1] == 'D'):
                count += 1
        elif len(face) == 3:
            if (face[0] == ':' or face[0] == ';') and (face[1] == '-' or face[1] == '~') and (face[2] == ')' or face[2] == 'D'):
                count += 1
    return count
