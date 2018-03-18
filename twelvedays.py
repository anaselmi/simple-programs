#July 11, 2017
#Prints the lyrics to twelve days of christmas
numbers = {
1: "first",
2: "second",
3: "third",
4: "fourth",
5: "fifth",
6: "sixth",
7: "seventh",
8: "eight",
9: "ninth",
10: "tenth",
11: "eleventh",
12: "twelfth"
}

gifts = [ 
"Partridge in a Pear Tree",
"Turtle Doves",
"French Hens",
"Calling Birds",
"Golden Rings",
"Geese a Laying",
"Swans a Swimming",
"Maids a Milking",
"Ladies Dancing",
"Lords a Leaping",
"Pipers Piping",
"Drummers Drumming"]

for item in range(1, 13):
    print("On the the %s day of Christmas" %(numbers[item]))
    print("my true love sent to me:")

    if item >= 12:
        print("twelve %s" %(gifts[11]))

    if item >= 11:
        print("eleven %s" %(gifts[10]))

    if item >= 10:
        print("ten %s" %(gifts[9]))

    if item >= 9:
        print("nine %s" %(gifts[8]))

    if item >= 8:
        print("eight %s" %(gifts[7]))

    if item >= 7:
        print("seven %s" %(gifts[6]))

    if item >= 6:
        print("six %s" %(gifts[5]))

    if item >= 5:
        print("five %s" %(gifts[4]))

    if item >= 4:
        print("four %s" %(gifts[3]))

    if item >= 3:
        print("three %s" %(gifts[2]))

    if item >= 2:
        print("two %s" %(gifts[1]))

    if item == 1:
        print("a %s" %(gifts[0]))
    else:
        print("and %s" %(gifts[0]))
    
    print()
    print()