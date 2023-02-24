def what_century(year):
    century = (int(year) - 1) // 100 + 1
    if century % 100 in [11, 12, 13]:
        suffix = "th"
    else:
        last_digit = century % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"
    return str(century) + suffix