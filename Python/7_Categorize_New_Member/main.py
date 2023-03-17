# 7 kyu - Categorize New Member

def categorize_members(members):
    result = []
    for member in members:
        age, handicap = member
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
