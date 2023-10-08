def fib():
    back1, back2 = 0, 1
    while True:
        yield back1
        back1, back2 = back2, back1 + back2

f = fib()
for i in range(20):
    print(next(f))
