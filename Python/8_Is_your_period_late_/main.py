# 8 kyu - Is your period late?
def period_is_late(last, today, cycle_length):
    one_day = 24 * 60 * 60 # количество секунд в дне
    days_passed = (today - last).days # получаем количество дней между датами
    return days_passed > cycle_length