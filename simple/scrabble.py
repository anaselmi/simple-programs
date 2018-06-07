def scrabble(letters, word):
    word = [x for x in word]
    letters = [x for x in letters]
    
    for letter in word:
        if letter not in letters:
            if "?" in letters:
                letters.remove("?")
            else:
                return False
        else:
            letters.remove(letter)
    return True
