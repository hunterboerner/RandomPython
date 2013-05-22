
inputint = 1
stop = False
while stop == False:
	inputint = input("Enter a number: ")
	if inputint == 0:
		stop = True
	x = ""
	while inputint>0:
		if inputint-100==0:
			x = "" + "C"
			inputint=inputint-100
			pass
		elif inputint-90>=0:
			inputint=inputint-90
			x=x+"XC"
			pass
		elif inputint-50>=0:
			x=x+"L"
			inputint=inputint-50
			pass
		elif inputint-40>=0:
			x = x+"XL"
			inputint=inputint-40
			pass
		elif inputint-10>=0:
			x = x+"X"
			inputint=inputint-10
			pass
		elif inputint-9>=0:
			x=x+"IX"
			inputint=inputint-9
			pass
		elif inputint-5>=0:
			x=x+"V"
			inputint=inputint-5
			pass
		elif inputint-4>=0:
			x=x+"IV"
			inputint=inputint-4
			pass
		elif inputint-1>=0:
			x=x+"I"
			inputint=inputint-1
			pass
	if stop == False:
		print x
	pass


	# 100
	# 90
	# 50
	# 40
	# 10
	# 9
	# 5
	# 4
	# 1
