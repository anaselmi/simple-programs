from functools import reduce

def is_latin_square(n, latin):
	latin = [int(x) for x in latin if x != " "]
	if len(latin) != n*n:
		return False
	uniques = []
	for number in latin:
		if number not in uniques:
			uniques.append(number)
	if len(uniques) != n:
		return False
	uniques_sum = reduce((lambda x, y: x+y), uniques)
	#If we have n items, and n of each item, then the sum of all items should equal the sum of uniques * n
	if reduce((lambda x, y: x + y), latin) != uniques_sum * n:
		return False
	columns = []
	for i, number in enumerate(latin):
		if i < n:
			columns.append([number])
			row_start = i * n
			row_end  = row_start + n
			#Also, the sum of each row should equal the sum of all uniques
			if reduce((lambda x, y: x + y), latin[row_start: row_end]) != uniques_sum:
				return False
			continue
		current_column = i % n
		columns[current_column][0] += number
	#The sum of all columns should also equal the sum of all uniques
	for item in columns:
		if item[0] != uniques_sum:
			return False
	return True

print(is_latin_square(5, "1234523451345124512351243"))

		
	