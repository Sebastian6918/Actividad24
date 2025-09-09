def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)


