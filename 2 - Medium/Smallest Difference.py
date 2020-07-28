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

