#filename:sorting.py
#author:Randy Hollensbe

import random

l=[]
s=[]

rng=input("What is the range of number? ")
num=input("How many elements? ")

checkValue = rng + 1

for i in range(0,num):
    l.append(random.randint(1,rng))
for x in xrange(len(l)):
	for x2 in xrange(len(l)):
		if l[x2] < checkValue:
			checkValue = l[x2]
	l.remove(checkValue)
	s.append(checkValue)
	checkValue = rng + 1
print l
print s

# create your sort here
