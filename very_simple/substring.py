from string import ascii_uppercase


LETTERS = [x for x in ascii_uppercase]
VOWELS = ["A", "E", "I", "O", "U"]
CONSONANTS = [x for x in LETTERS if x not in VOWELS]


def substring(string):
    letters = [x for x in string.upper()]
    consonants_sum = vowels_sum = 0
    for i, x in enumerate(reversed(letters)):
        score = i + 1
        if x in CONSONANTS:
            consonants_sum += score
        else:
            vowels_sum += score

    if consonants_sum > vowels_sum:
        print("Stuart %s" % consonants_sum)
    elif vowels_sum > consonants_sum:
        print("Kevin %s" % vowels_sum)
    else:
        print("Draw.")
