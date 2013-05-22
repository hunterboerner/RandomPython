inputsize = input("Enter a number for your size: ")
character = raw_input('Enter a character for the shape of the diamond: ')

size = inputsize
spacing = 0
first = True
result = []
while size != 0:
	if first == True:
		print(" " * size + character)
		result.append(" " * size + character)
		size = size - 1
		print(" " * size + character + " " + character)
		result.append(" " * size + character + " " + character)
		spacing = spacing + 1

	if first == False:
		print(" " * size + character + (" " * spacing) + character)
		result.append(" " * size + character + (" " * spacing) + character)
	first = False
	size = size - 1
	spacing = spacing + 2
for x in xrange(inputsize-1):
	print result[inputsize-x-2]
