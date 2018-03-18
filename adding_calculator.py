def calculator(uncalculated):
    for i, letter in enumerate(uncalculated):
        if i == 0:
            continue
        if letter == "+":
            operation = "+"
            index = i
            break
        if letter == "-":
            operation = "-"
            index = i
            break
        if letter == "*":
            operation = "*"
            index = i
            break
        if letter == "/":
            operation = "/"
            index = i
            break
        if letter == "^":
            operation = "^"
            index = i
            break
    if  operation == "+":
        int1 = int(uncalculated[0:index])
        int2 = int(uncalculated[index + 1:])
        total = int(int1) + int(int2)
        return total

    if  operation == "-":
        int1 = int(uncalculated[0:index])
        int2 = int(uncalculated[index + 1:])
        total = int1 +-int2
        return total

    if  operation == "*":
        int1 = int(uncalculated[0:index])
        int2 = int(uncalculated[index + 1:])
        if (int1 < 0) != (int2 < 0):
            negative = True
        else:
            negative = False
        if int1 < 0:
            int1 = int(str(int1)[1:])
        if int2 < 0:
            int2 = int(str(int2)[1:])
        step = 0
        total = 0
        while step < int2:
            total += int1
            step += 1
        if negative == True:
            total = -total
        return total

    if  operation == "/":
        int1 = int(uncalculated[0:index])
        int2 = int(uncalculated[index + 1:])
        if int2 == 0:
            return "fuk u"
        if (int1 < 0) != (int2 < 0):
            negative = True
        else:
            negative = False
        if int1 < 0:
            int1 = int(str(int1)[1:])
        if int2 < 0:
            int2 = int(str(int2)[1:])
        count = int1
        total = 0
        while count > 0:
            count -= int2
            total +=1
        else:
            if count != 0:
                return "NON-INTEGRAL ANSWER"
        if negative == True:
            print(negative)
            total = -total
        return total

    if  operation == "^":
        index = uncalculated.index("^")
        int1 = int(uncalculated[0:index])
        int2 = int(uncalculated[index + 1:])
        total = 1
        if int2 == 0:
            return total
        for power in range(0, int2 + 1):
            if power == 0:
                continue
            adding_total = 0
            for x in range(0, int1):
                adding_total += total
            total = adding_total
            
        return total

print(calculator("3+5"))
print(calculator("9*3"))
print(calculator("9*-3"))                               
print(calculator("2-5"))
print(calculator("12/2"))
print(calculator("9^2")) 
print(calculator("2/7"))
print(calculator("124^0"))
print(calculator("1^1"))

