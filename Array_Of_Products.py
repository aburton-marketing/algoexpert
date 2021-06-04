def proArray(array, i):
	mSum = 1
	for x in range(len(array)):
		if x != i:
			mSum *= array[x]
			print(array[x], mSum, i)
	print(array)
	return mSum

def arrayOfProducts(array):
	n = []
    for i in range(len(array)):
		n.append(proArray(array, i))
	return n
