# My attempt: O(n) time | O(1) space
def findThreeLargestNumbers(array):
	maxThree = []
	for num in array:
		if len(maxThree) < 3:
			maxThree.append(num)
		else:
			# indxe() and min() are constant time operations because the maxThree array length is <= 3
			indexOfMin = maxThree.index(min(maxThree))  
			print(maxThree)
			if num >= maxThree[indexOfMin]:
				maxThree[indexOfMin] = num
	# sorting is a constant time operations because the maxThree array length is <= 3
	maxThree.sort()
	return maxThree

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(1) space
def findThreeLargestNumbers(array):
	threeLargest = [None, None, None]
	for num in array:
		updateLargest(threeLargest, num)
	return threeLargest

def updateLargest(threeLargest, num):
	# iterate through threeLargest array from right to left
	for idx in range(len(threeLargest)-1, -1, -1):
		# if the number is larger than the number in threeLargest array, call the shift function
		#   to update threeLargest
		if threeLargest[idx] is None or num > threeLargest[idx]:
			shiftAndUpdate(threeLargest, num, idx)
			break
		idx = idx + 1
	
def shiftAndUpdate(array, num, idx):
	# shift all the numbers from index 0 to idx-1 left, set number at index idx to num
	# example:
	# num 4
	# idx:  0 1 2
	# arr: [1,2,3]
	# shift: [2,2,3] -> [2,3,3] -> [2,3,4]
	for i in range(idx + 1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i + 1]
		