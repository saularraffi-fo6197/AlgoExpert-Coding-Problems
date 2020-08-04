def spiralTraverse(array):
	spiralArray = []
	
    leftBound = 0
	topBound = 0
	rightBound = len(array[0]) - 1
	bottomBound = len(array) - 1
	
	while bottomBound > topBound or rightBound > leftBound:
		for i in range(leftBound, rightBound + 1):
			print(array[topBound][i])
			spiralArray.append(array[topBound][i])
		topBound += 1
		for i in range(topBound, bottomBound + 1):
			print(array[i][rightBound])
			spiralArray.append(array[i][rightBound])
		rightBound -= 1
		for i in reversed(range(leftBound, rightBound + 1)):
			print(array[bottomBound][i])
			spiralArray.append(array[bottomBound][i])
		bottomBound -= 1
		for i in reversed(range(topBound, bottomBound + 1)):
			print(array[i][leftBound])
			spiralArray.append(array[i][leftBound])
		leftBound += 1

	return spiralArray
