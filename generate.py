def generate(num):
    assert(num >= 1)
    for x in range(1, num + 1):
        print(x)


num = int(input("Enter number: \n"))
generate(num)