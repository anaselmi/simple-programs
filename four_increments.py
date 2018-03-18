#June 24, 2017
#This function looks at a list of four and checks to see if each item increments by 1 
def is_it_four(original):
	if len(original) == 4:
		return True
	else:
		return False

original = [2, 3, 4, 6]



def four_increments(original):
	right_length = is_it_four(original)
	if right_length == False:
		return False
	else:
		mid = sorted(original)
		for i, item in enumerate(mid):
			if i == 0:
				pass
			else:
				if mid[i] == mid[i - 1] + 1:
					pass
				else:
					return False
					break


		return True


print(four_increments(original))





