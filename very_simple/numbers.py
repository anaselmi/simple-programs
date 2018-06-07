numbers = []
print("Give me numbers! Type done if you're done.")

while True:
    number = input("Go ahead: ")
    if number.lower() == "done":
        break
    numbers.append(int(number))


print(numbers)
