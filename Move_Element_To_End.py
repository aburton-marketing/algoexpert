def moveElementToEnd(array, toMove):
	changed = 0
	counter = 1
	tmc = 0
    while True:
		print(array, changed)
    # Swap values
		for i in range(len(array)-counter):
			if array[i] == toMove:
				array[i], array[i+1] = array[i+1], array[i]
				tmc += 1
		# Increment counter
    counter += 1
    # The changed variable helps us stop the loop early to increse speed
		if changed != tmc:
			changed = tmc
		elif changed == tmc:
			break
	return array
