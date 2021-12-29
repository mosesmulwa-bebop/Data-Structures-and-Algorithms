def factorial(n):
    """ This returns the factorial of a number recursively """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
