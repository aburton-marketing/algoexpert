def minimumWaitingTime(queries):
	queries.sort()
	times = []
	cursum = 0
	for i in range(len(queries)):
		back = i - 1
		if i == 1:
			times.append(queries[0])
			cursum = queries[0]
		if i >= 2:
			cursum += queries[back] 
			times.append(cursum)	
    return sum(times)
