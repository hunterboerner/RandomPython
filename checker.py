
dim = input("Enter a number: ")
board = {}

def boardGen(dim, alternate):
	total = ""
	black = "#" * dim
	white = "." * dim

	if alternate == True:
		total = black + white
	else:
		total = white + black

	total = total * 4
	return total

for x in xrange(8):
	for y in xrange(dim):
		print boardGen(dim, (x % 2) == 0)
