# September 1, 2017
# Checks if a string is valid dna and returns the amount of each letter

def dna_letter_frequency(s):
	a_count = 0
	c_count = 0
	g_count = 0
	t_count = 0
	for letter in s:
		if letter.lower() == "a":
			a_count += 1
		elif letter.lower() == "c":
			c_count += 1
		elif letter.lower() == "g":
			g_count += 1
		elif letter.lower() == "t":
			t_count += 1
		else:
			return "Not a valid DNA sequence."
	return "{a} {c} {g} {t}".format(a = a_count, c = c_count, g = g_count, t = t_count)

print(dna_letter_frequency("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))
