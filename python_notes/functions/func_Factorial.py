# Factorial functions: calling itself over&over again, breaking down problem
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(2))