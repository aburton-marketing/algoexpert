def twoNumberSum(array, targetSum):
	targetSumPair = []
    for i in range(len(array)-1):
		j = i + 1
		for j in range(len(array)):
			if array[i] + array[j] == targetSum and i != j:
				targetSumPair.append(array[i])
				targetSumPair.append(array[j])
				return targetSumPair
	return targetSumPair
