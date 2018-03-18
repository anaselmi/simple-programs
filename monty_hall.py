import random
while True:
    print("Welcome to Monty Hall. There are three doors in front of you, one of them leads to a brand new car, the other two lead to goats.")
    car_door = random.randrange(1,4)
    try:
       user_pick = int(input("Which door would you like to pick?\n"))
    except ValueError:
        print("That's not a number, try again.")
        continue
    if user_pick > 3 or user_pick < 1:
        print("That's not a number between 1 and 3, try again.")
        continue
    open_door = random.choice([x for x in range(1, 4) if x != user_pick and x != car_door])
    swap_door = [x for x in range(1, 4) if x != open_door and x != user_pick][0]
    while True:
        swap = input("There was a goat behind door %d. Would you like to swap to door %d?\n" %(open_door, swap_door)).lower()
        if swap == "y" or swap == "yes":
            user_pick = swap_door
            print("Alright, you've chosen to swap doors.")
            break
        elif swap == "n" or swap == "no":
            print("Alright, you've chosen not to swap doors")
            break
        else:
            print("I'm afraid I didnt understand you. Please answer yes or no.")
    if car_door == user_pick:
        print("You've won! The car was behind door %d just like you guessed" %(car_door))
    else:
        print("You lost! The car was actually behind door %d" %(car_door))
        


