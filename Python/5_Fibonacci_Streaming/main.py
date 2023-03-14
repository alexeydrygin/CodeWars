# 5 kyu - Fibonacci Streaming
def all_fibonacci_numbers():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

fib = all_fibonacci_numbers()
for i in range(10):
    print(next(fib))