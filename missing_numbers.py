#June 27, 2017
#Shows numbers missing in sequence
#NEED TO COMMENT THIS
def missing_numbers(numbers):
    mid = numbers
    final = []
    #We sort our numbers to get the lowest and highest numbers
    mid.sort()
    last_number = mid[-1]
    #We make a list that includes all numbers between our lowest and highest numbers
    full_numbers = range(1, last_number)
    #This looks at mid, and if a number isn't there, that means it's missing and we need to add it to final
    for number in full_numbers:
        if number not in mid:
            final.append(number)
    print(full_numbers)
    return final

list = [99]
print(missing_numbers(list))