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
oppTurn = 'X'
start0 = [' ',' ',' ','O','X',' ',' ',' ',]	
start1 = [' ',' ',' ','X','O',' ',' ',' ',]
board = []
play = True

def switch():
	global turn
	if turn == 'O':
			turn = 'X'
			oppTurn = 'O'
	elif turn == 'X':
		turn = 'O'
		oppTurn = 'X'

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
		if board[int(inputListRaw[1])-1][inputList[0]-1] != (turn or oppTurn):
			board[int(inputListRaw[1])-1][inputList[0]-1] = turn
		switch()