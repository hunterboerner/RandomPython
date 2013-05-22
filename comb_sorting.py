#filename:sorting.py
#author:Randy Hollensbe

import random

l = []

rng=input("What is the range of number? ")
num=input("How many elements? ")


for i in range(0,num):
    l.append(random.randint(1,rng))

swapped = False
gap = len(l)
iterations = 0

print gap, swapped

while ((gap != 1) or swapped == True):
	gap = int(gap/1.3)
	if gap < 1:
		gap = 1

	i = 0
	swapped = False
	
	while (i + gap) < len(l):
		if l[i] > l[i+gap]:
			tmp = l[i+gap]
			l[i+gap] = l[i]
			l[i] = tmp
			swapped = True
			iterations = iterations + 1
		i = i + 1

print l
print iterations

# create your sort here
