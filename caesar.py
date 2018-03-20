# August 23, 2017
# Caesar encryption and decryption
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def caesar(message, shift):
    result = []
    for char in message:
        if char == " ":
            result.append(" ")
        else:
            i = alphabet.index(char)
            i += shift
            i = i % 26
            new_char = alphabet[i]
            result.append(new_char)
    return result


def reverse_caesar(message, shift):
    result = []
    for char in message:
        if char == " ":
            result.append(" ")
        else:
            i = alphabet.index(char)
            i -= shift
            i = i % 26
            new_char = alphabet[i]
            result.append(new_char)
    return result
