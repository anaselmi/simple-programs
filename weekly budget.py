# May 22, 2017
# Program to find out how much I made in a week as a window installer.
def weekly_budget(hours, overtime = 0):
	number = (hours * 15) + (overtime * (15 + 15 / 2))
	print("You made %d$ this week." % (number))

print(weekly_budget(8))