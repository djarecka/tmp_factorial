def my_factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
def my_factorial(n):
    if n < 0:
        raise Exception("factorial can be calculated only for positive numbers")

    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
