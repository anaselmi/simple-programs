def in_range(first, last, number):
    print(range(first, last))
    if number in range(first + 1, last):
        return True
    else:
        return False
