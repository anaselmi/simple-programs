import time
import sys


word = "Hello World"
current_word = ["" for _ in range(len(word))]

for i, letter in enumerate(current_word):
    for ordinal in range(32, 123):
        current_word[i] = character = chr(ordinal)
        sys.stdout.write('\r'+"".join(current_word))
        sys.stdout.flush()
        time.sleep(0.01)
        if current_word[i] == word[i]:
            break
