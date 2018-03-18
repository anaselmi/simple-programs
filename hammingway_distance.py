#June 27, 2017
#Gives the distance between two equal length words
#NEED TO COMMENT THIS
from time import sleep
first_time = True
while True:
    if first_time:
        print("Welcome to Hammingway Distance. Give me two words, and I'll tell you how many characters are different between them!")
    else:
        print("Welcome back to Hammingway Distance. Give me two words, and I'll tell you how many characters are different between them!")
    word_1 = input("What's your first word?: ")
    word_2 = input("What's your second word?: ")
    distance = 0
    
    if len(word_2) != len(word_1):
        print("Those words aren't the same length. Please try again.")
    else:
        for i, letter in enumerate(word_1):
            if word_1[i] != word_2[i]:
                distance += 1
            pass
        
        print("The distance is %d" %(distance))
    first_time = False
    sleep(1)
    