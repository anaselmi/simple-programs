def factorial(number):
    factored = 1
    for n in range(1, number + 1):
        factored = factored * n
    return factored

print(factorial(9))