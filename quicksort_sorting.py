#filename:sorting.py
#author:Randy Hollensbe

import random

l = []

rng=input("What is the range of number? ")
num=input("How many elements? ")

checkValue = rng + 1

for i in range(0,num):
    l.append(random.randint(1,rng))
iterations = 0
def quicksort(li):
	global iterations

	small = []
	large = []

	if len(li) <= 1:
		return li
	pivot = li[0]
	li.remove(pivot)
	for x in xrange(len(li)):
		iterations += 1
		if li[x] <= pivot:
			small.append(li[x])
		else:
			large.append(li[x])
	pivot1=[]
	pivot1.append(pivot)
	return quicksort(small) + pivot1 + quicksort(large)
print quicksort(l)
print "It has iterated: " + str(iterations) + " times"

# create your sort here
