# My Attempt 1: O(nlog(m)) time | O(1) space
#   Where n is arrayOne and m is arrayTwo
def smallestDifference(arrayOne, arrayTwo):
	arrayTwo.sort()
	minDiff = float("inf")
	minDiffNums = []
	for num in arrayOne:
		localMinDiffNums = binarySearchForMinDiff(arrayTwo, num)
		if abs(localMinDiffNums[0] - localMinDiffNums[1]) == 0:
			return localMinDiffNums
		elif abs(localMinDiffNums[0] - localMinDiffNums[1]) < minDiff:
			minDiffNums = localMinDiffNums
			minDiff = abs(localMinDiffNums[0] - localMinDiffNums[1])
	return minDiffNums
		
def binarySearchForMinDiff(array, key):
	left = 0
	right = len(array) - 1
	minDiff = float("inf")
	minDiffNums = []
	
	while left <= right:
		middle = (left + right) // 2
		diff = abs(key - array[middle])
		if diff == 0:
			return [key, array[middle]]
		if diff < minDiff:
			minDiff = diff
			minDiffNums = [key, array[middle]]
		if key > array[middle]:
			left = middle + 1
		else:
			right = middle - 1
	
	return minDiffNums

# ================================================================================================

# My Attempt 2: O(nlog(n)) + O(mlog(m)) time | O(1) space
#   Where n is the length of the first array and m is the length of the second array
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	length = len(arrayOne) + len(arrayTwo) - 1
	minDiff = float("inf")
	minDiffNums = []
	
	idx1, idx2, i = 0, 0, 0
	while i < length:
		idx1 = len(arrayOne) - 1 if idx1 >= len(arrayOne) else idx1
		idx2 = len(arrayTwo) - 1 if idx2 >= len(arrayTwo) else idx2
					
		diff = abs(arrayOne[idx1] - arrayTwo[idx2])
		
		if diff == 0:
			return [arrayOne[idx1], arrayTwo[idx2]]
		elif diff < minDiff:
			minDiff = diff
			minDiffNums = [arrayOne[idx1], arrayTwo[idx2]]
		
		if arrayOne[idx1] < arrayTwo[idx2]:
			idx1 += 1
		else:
			idx2 += 1
		i += 1
			
	return minDiffNums

# ================================================================================================

# AlgoExpert solution 1: O(nlog(n)) + O(mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	current = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo += 1 
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current 
			smallestPair = [firstNum, secondNum]
	return smallestPair