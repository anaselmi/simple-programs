# May 26, 2017
# Tells you how much something costs and if it's in stock.
def stock_check(item):
	in_stock = False
	
	for choice in stock:
		if item == choice:
			in_stock = True
			break
	
	if in_stock == False:
		print("I'm afraid we don't have that in stock.")
	else:
		print("Did you say %s? That'll be %d$." 
			% (item, stock[item]))


stock = {
"lamb" : 9.50,
"beef" : 7.30,
"chicken" : 5.00,
}

stock_check("lamb")
