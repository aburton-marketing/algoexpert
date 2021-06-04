
def classPhotos(redShirtHeights, blueShirtHeights):
	
	redShirtHeights.sort()
	blueShirtHeights.sort()
	
	if sum(redShirtHeights) > sum(blueShirtHeights):
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] < blueShirtHeights[i]:
				return False
			elif redShirtHeights[i] == blueShirtHeights[i]:
				return False
			elif redShirtHeights[i] > blueShirtHeights[i]:
				if i == len(blueShirtHeights) - 1:
					return True
    elif sum(blueShirtHeights) > sum(redShirtHeights):
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i] < redShirtHeights[i]:
                return False
			elif blueShirtHeights[i] == redShirtHeights[i]:
				return False
			elif blueShirtHeights[i] > redShirtHeights[i]:
				if i == len(blueShirtHeights) - 1:
					return True
    elif sum(blueShirtHeights) == sum(redShirtHeights):
        for i in range(len(blueShirtHeights)):
			if blueShirtHeights[i] == redShirtHeights[i]:
				return False
			elif blueShirtHeights[i] > redShirtHeights[i]:
				if i == len(blueShirtHeights) - 1:
					return True
