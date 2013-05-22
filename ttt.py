# Create an arrary for the Board
# Create vars

import random
import os
import time



sboard = [0,0,0,0,0,0,0,0,0]
while True:
	time.sleep(1)
	print 'Iterate'
	board = [0,0,0,0,0,0,0,0,0]
	inBoard = open('//WDMYBOOKLIVE/Public/Shared Data/Classes/IndependentStudyTheron/ttt.txt','r')
	xNum = 0
	oNum = 0	
	rand = random.randint(1,8)
	#Import to the board var
	for x in xrange(9):
		board[x] = inBoard.readline(1)
	inBoard.close()
	if sboard != board:
		time.sleep(1)
		sboard = board
		turnChar = 'X'
		oppTurnChar = 'O'
		done = False
		for x in xrange(9):
			if board[x] == "X":
				xNum = xNum + 1
			elif board[x] == "O":
				oNum = oNum + 1
		if xNum == 0:
			board[random.randint(1,8)] = "X"
			xNum = xNum + 1
			done = True
		if oNum == 0 and done == False:
			while board[rand] == 'X':
				rand = random.randint(1,8)
			board[rand] = "O"
			oNum = oNum + 1
			done = True

		#decide where and when to go

		x = 0
		move = False
		place = 0

		#Left
		if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
			print "We have a winner... X!"
			done = True

		#Diagonal from up left to low right	
		elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
			print "We have a winner... X!"
			done = True

		#Top
		elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
			print "We have a winner... X!"
			done = True

		#Bottom
		elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
			print "We have a winner... X!"
			done = True

		#Diagonal from Up right to low left
		elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
			print "We have a winner... X!"
			done = True

		#Right
		elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
			print "We have a winner... X!"
			done = True

		#Middle Down
		elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
			print "We have a winner... X!"
			done = True

		#Middle Sideways
		elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
			print "We have a winner... O!"
			done = True
		elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
			print "We have a winner... X!"
			done = True

		if xNum != 0 and oNum != 0 and done == False:
			if xNum == oNum:
				turnChar = 'X'
				oppTurnChar = 'O'
			else:
				turnChar = 'O'
				oppTurnChar = 'X'
			while x != 9:
				if board[x] == oppTurnChar:
					#top
					if x == 0:
						if board[x + 1] == oppTurnChar and board[x + 2] != turnChar:
							board[x + 2] = turnChar
							x = 9
							print 'test1'
						elif board[x + 2] == oppTurnChar and board[x + 1] != turnChar:
							board[x + 1] = turnChar
							x = 9
							print 'test2'
						#Up right low left
						elif board[x + 4] == oppTurnChar and board[x + 8] != turnChar:
							board[x + 8] = turnChar
							x = 9
							print 'test3'
						elif board[x + 8] == oppTurnChar and board[x + 4] != turnChar:
							board[x + 4] = turnChar
							x = 9
							print 'test4'
						#Left vert
						elif board[x + 3] == oppTurnChar and board[x + 6] != turnChar:
							board[x + 6]  = turnChar
							x = 9
							print "test5"
						elif board[x + 6] == oppTurnChar and board[x + 3] != turnChar:
							board[x + 3] = turnChar
							x = 9
							print 'test6'
						else:
							x = x + 1
							print 'else1'
					elif x == 4:
						if board[x + 4] == oppTurnChar and board[x - 4] != turnChar:
							board[x - 4] = turnChar
							x = 9
							print 'test7'
						elif board[x - 4] == oppTurnChar and board[x + 4] != turnChar:
							board[x + 4] = turnChar
							x = 9
							print 'test8'
						elif board[x + 3] == oppTurnChar and board[x - 3] != turnChar:
							board[x - 3] = turnChar
							x = 9
							print 'test9'
						elif board[x - 3] == oppTurnChar and board[x + 3] != turnChar:
							board[x + 3] = turnChar
							x = 9
							print 'test10'
						elif board[x - 1] == oppTurnChar and board[x + 1] != turnChar:
							board[x + 1] = turnChar		
							x = 9
							'derp'
						elif board[x + 1] == oppTurnChar and board[x - 1] != turnChar:
							board[x - 1] = turnChar
							x = 9
							print 'herp'
						elif board[x - 2] == oppTurnChar and board[x + 2] != turnChar:
							board[x + 2] = turnChar
							x = 9
							print 'hello'
						elif board[x + 2] == oppTurnChar and board[x - 2] != turnChar:
							board[x - 2] = turnChar
							x = 9
							print 'howdy'
						else:
							x = x + 1
							print 'else2'
					elif x == 3:
						if board[x + 3] == oppTurnChar and board[x - 3] != turnChar:
							board[x - 3]  = turnChar
							x = 9
							print 'test11'
						elif board[x - 3] == oppTurnChar and board[x + 3] != turnChar:
							board[x + 3] = turnChar
							x = 9
							print 'test12'
						elif board[x + 1] == oppTurnChar and board[x + 2] != turnChar:
							board[x + 2] = turnChar
							x = 9
							print 'doitwork???'
						elif board[x + 2] == oppTurnChar and board [x + 1] != turnChar:
							board[x + 1] = turnChar
							x = 9
							print 'lawl'
						else:
							x = x + 1
							print 'else3'
					# up right, low left
					elif x == 2:
						if board[x + 3] == oppTurnChar and board[x + 6] != turnChar:
							board[x + 6] = turnChar
							x = 9
							print 'test13'
						elif board[x + 6] == oppTurnChar and board[x + 3] != turnChar:
							board[x + 3] = turnChar
							x = 9
							print 'test14'
						elif board[x + 2] == oppTurnChar and board[x + 4] != turnChar:
							board[x + 4] = turnChar
							x = 9
							print 'HEEEEEEYYY'
						elif board[x + 4] == oppTurnChar and board[x + 2] != turnChar:
							board[x + 2] = turnChar
							x = 9
							print 'jdfkjdfjk'
						else:
							x = x + 1
							print 'else4'
					elif x == 5:
						if board[x + 3] == oppTurnChar and board[x - 3] != turnChar:
							board[x - 3] = turnChar
							x = 9
							print 'test15'
						elif board[x - 3] == oppTurnChar and board[x + 3] != turnChar:
							board[x + 3] = turnChar
							x = 9
							print 'test16'
						else:
							x = x + 1
							print 'else5'
					#bottom
					elif x == 6:
						if board[x + 1] == oppTurnChar and board[x + 2] != turnChar:
							board[x + 2] = turnChar
							x = 9
							print 'test17'
						elif board[x + 2] == oppTurnChar and board[x + 1] != turnChar:
							board[x + 1] = turnChar
							x = 9
							print 'test18'
						else:
							x = x + 1
							print 'else6'
					elif x == 7:
						if board[x + 1] == oppTurnChar and board[x - 1] != turnChar:
							board[x - 1] = turnChar
							x = 9
							print 'test19'
						elif board[x - 1] == oppTurnChar and board[x + 1] != turnChar:
							board[x + 1] = turnChar
							x = 9
							print 'test20'
						else:
							x = x + 1
							print 'else7'
					#vertical right
					
					
					#vertical middle
					elif x == 1:
						if board[x + 3] == oppTurnChar and board[x + 6] != turnChar:
							board[x + 6]  = turnChar
							x = 9
							print 'test21'
						elif board[x + 6] == oppTurnChar and board[x + 3] != turnChar:
							board[x + 3] = turnChar
							x = 9
							print 'test22'
						elif board[x + 1] == oppTurnChar and board[x - 1] != turnChar:
							board[x - 1] = turnChar
							x = 9
							print 'test23'
						elif board[x - 1] == oppTurnChar and board[x + 1] != turnChar:
							board[x + 1] = turnChar
							x = 9
							print 'test24'
						else:
							x = x + 1
							print 'else8'
					else:
						x = x + 1
				elif (x == 8 and board[x] != turnChar) or (xNum + oNum) == 8:
						while board[rand] == oppTurnChar or board[rand] == turnChar:
							rand = random.randint(1,8)
						board[rand] = turnChar
						x = 9
						print 'randomness'
				else:
					x = x + 1
					print 'totalelseness'
				
							



		#print the board
		print board[0] + " " + board[1] + " " + board[2]
		print board[3] + " " + board[4] + " " + board[5]
		print board[6] + " " + board[7] + " " + board[8]

		outBoard = open('//WDMYBOOKLIVE/Public/Shared Data/Classes/IndependentStudyTheron/ttt.txt','w')
		outString = ''
		for x in xrange(9):
			outString=outString + board[x]
		outBoard.write(outString)
		outBoard.close()
	