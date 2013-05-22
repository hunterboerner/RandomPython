#filename:sorting.py
#author:Randy Hollensbe

import random

l = []

rng=input("What is the range of number? ")
num=input("How many elements? ")

checkValue = rng + 1

for i in range(num):
    l.append(random.randint(1, rng))

x = len(l) - 1
while x != 0:
	x = len(l) - 1
	for q in xrange(len(l)-1):
		if l[q] > l[q+1]:
			tmp = l[q+1]
			l[q+1] = l[q]
			l[q] = tmp
			x += 1
			print x

		else:
			x -= 1
			print x

print l

# create your sort here
