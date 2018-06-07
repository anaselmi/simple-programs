def reverse(string):
    final = ""
    for letter in string:
        final = letter + final
    return final
