# 6 Kyu - Playing with digits

def dig_pow(n, p):
    digits = [int(d) for d in str(n)]
    s = sum([d**(p+i) for i,d in enumerate(digits)])
    if s % n == 0:
        return s // n
    else:
        return -1