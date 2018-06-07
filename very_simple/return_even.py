def return_even(list):
    final = []
    for number in list:
        if number % 2 == 0:
            final.append(number)
    return final

list = [6, 9, 3, 4, 5, 6]
print(return_even(list))