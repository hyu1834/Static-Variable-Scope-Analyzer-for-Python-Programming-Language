def sumOfOdds(range):
	sum_odd = 0
	index = 1
	while(index <= range):
		if(index % 2 == 1):
			sum_odd += index
		index += 1

	return sum_odd

def productOfPowersOf2(exp1, exp2):
	if(exp1 < 0):
		return

	product = 1
	while(exp1 <= exp2):
		exp1 += 1
	return product

def printAsterisks(amount):
	if(amount < 0):
		return
	index = 1
	while(index < amount):
		index += 1

def printTriangle(amount):
	if(amount < 0):
		return

	index = 1
	while(index <= amount):
		index2 = 0
		while(index2 < index):
			index2 += 1
		index += 1