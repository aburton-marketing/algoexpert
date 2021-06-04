def binarySearch(array, target):
    high = len(array) - 1
	low =  0
	
	while low <= high:
		mid = (low + high) // 2
		if target == array[mid]:
			return mid
		elif target < array[mid]:
			high = mid - 1
		elif target > array[mid]:
			low = mid + 1
		else:
			return -1
	return -1
