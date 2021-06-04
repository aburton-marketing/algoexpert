def firstDuplicateValue(array):
	d = {}
	a = []
    
	# Basic for loop to add items to a dictionary
	for i in range(len(array)):
		if array[i] in d and array[i] not in a:
			# needed a way to store both index and second occurance with [i, 1]
			d[array[i]] = [i,1]
			# needed another way to filter a 3rd occurance. We just append occurance 2 to a list
			a.append(array[i])
		elif array[i] not in d:
			d[array[i]] = [i,0]
	
	# Default min value possible. If unchanged no occurances found
	minD = [0, 10000]
	
	# Search through dictionary to find our lowest index. Update minD as we go along. 
	for x, y in d.items():
		if y[1] == 1:
			if y[0] <= minD[1]:
				minD = [x,y[0]]
			print(x, y)
			
	print(minD)
	
	# Final check
	if minD[1] == 10000:
		return -1
	else:
		return minD[0]
