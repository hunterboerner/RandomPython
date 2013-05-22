# Made by Theron Boerner
# Liscense:
#      DO WHAT THE F*** YOU WANT TO PUBLIC LICENSE 
#                    Version 2, December 2004 

# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

# Everyone is permitted to copy and distribute verbatim or modified 
	# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
	
#            DO WHAT THE F*** YOU WANT TO PUBLIC LICENSE 
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

#  0. You just DO WHAT THE F*** YOU WANT TO.

turn = "O"
start0 = [' ',' ',' ','O','X',' ',' ',' ',]	
start1 = [' ',' ',' ','X','O',' ',' ',' ',]
board = []
play = True

for x in xrange(3):
	board.append([' ',' ',' ',' ',' ',' ',' ',' ',])
board.append(start0)
board.append(start1)
for x in xrange(3):
	board.append([' ',' ',' ',' ',' ',' ',' ',' ',])

while play == True:
	printstring = ""
	for x in xrange(8):
		for y in xrange(8):
			printstring = printstring + '|' + board[x][y]
		printstring = printstring + '|'
		print printstring
		printstring = ""

	inputChar = raw_input("Input them commands: ")
	inputListRaw = list(inputChar)
	inputList = [ord(char) - 96 for char in inputChar.lower()]
	if inputChar == "END":
		play = False
	else:
		print board
		print inputList
		print inputListRaw
		board[int(inputListRaw[1])-1][inputList[0]-1] = turn
		if turn == 'O':
			turn = 'X'
		elif turn == 'X':
			turn = 'O'
		