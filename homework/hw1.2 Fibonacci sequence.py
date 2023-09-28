"""Fibonacci sequence"""


def fibo(n):
    l = list()
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        l = [1, 1]
        while n != len(l) - 1:
            l.insert(0, l[0] + l[1])
        return l


print(fibo(20))
