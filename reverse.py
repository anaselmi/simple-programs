#June 27, 2017
#Function that reverses a string
def reverse(string):
    final = ""
    for letter in string:
        final = letter + final
    return final


print(reverse("in the end it doesnt even matter! wow it actually"))
