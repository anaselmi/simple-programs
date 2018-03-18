#June 28, 2017
#Tells us whether or not a number is in range
def in_range(first, last, number):
    print(range(first, last))
    if number in range(first + 1, last):
        return True
    else:
        return False



print(in_range(1, 7, 1))
