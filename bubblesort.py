#June 17, 2017
#This function is a bubblesort that only looks at unsorted variables in a list
#NEED TO COMMENT THIS
def bubble_sort(unsorted):
    #This is the list we are trying to sort
    final = unsorted
    #This variable is used to make sure we aren't sorting what we've already sorted
    check = len(final) - 1
    done = False
    while done == False:
        try:
            #Reset swaps at the start of each loop
            swaps = 0
            for i, num in enumerate(final):
                #This code runs if we need to swap our unsorted numbes
                if final[i] > final[i + 1] and i <= check:
                    popped = final.pop(i)
                    final.insert(i + 1, popped)
                    swaps += 1
                #This runs at the end of the road
                elif i >= check:
                	#If we end our iteratation and haven't swapped, we're done
                    if swaps == 0:
                		done = True
                		break
                	#Otherwise we make check smaller and start again
                    else:
                		check -= 1
                		break
                #This runs if the numbers we're on are sorted
                else:
                    pass
        #Except only runs on our first loop
        except:
                if swaps == 0:
                	done = True
                	break
                else:
                	check -= 1
                	pass
    return final

print(bubble_sort([17, 21, 3, 4, 45, 3, 99, 1, 6, 2, 5, 3]))