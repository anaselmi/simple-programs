while True:
    source = input("What's your source?: \n")
    target = input("What's' your target?: \n")
    print()

    if len(source) != len(target):
        print("They're not the same length, please try again.")

    else:
        
        #Store letters in list so they can be edited
        final_list = [x for x in source]
        print("".join(final_list))

        #Changes letters one at a time, then prints current letters
        for i, letter in enumerate(final_list):
            if final_list[i] == target[i]:
                pass
            else:
                final_list[i] = target[i]
                print("".join(final_list))
        print()



