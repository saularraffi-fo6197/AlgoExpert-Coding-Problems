# My Attempt 1: O(n^3) time | O(n) space
def threeNumberSum(array, targetSum):
	tripletSums = []
    for idx1 in range(len(array) - 2):
		for idx2 in range(idx1 + 1, len(array) - 1):
			for idx3 in range(idx2 + 1, len(array)):
				if array[idx1] + array[idx2] + array[idx3] == targetSum:
					triplet = [array[idx1], array[idx2], array[idx3]]
					triplet.sort()
					tripletSums.append(triplet)
					print(tripletSums)
	tripletSums.sort()
	return tripletSums

# ================================================================================================

# My Attempt 2: O(n^3) time | O(n) space
def threeNumberSum(array, targetSum):
	tripletSums = []
    # sorting the array itself at the beginning eliminates the need to sort tripletSums at the end and
    #   triplet in our last for loop
	array.sort()
    for idx1 in range(len(array) - 2):
		for idx2 in range(idx1 + 1, len(array) - 1):
			for idx3 in range(idx2 + 1, len(array)):
				if array[idx1] + array[idx2] + array[idx3] == targetSum:
					triplet = [array[idx1], array[idx2], array[idx3]]
					tripletSums.append(triplet)
	return tripletSums

# ================================================================================================

# My Attempt 3: O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
	table = {}
	for num in array:
		table[num] = True	
	
	tripletSums = []
	array.sort()
	for idx1 in range(len(array) - 2):
		for idx2 in range(idx1 + 1, len(array) - 1):
			diff = targetSum - (array[idx1] + array[idx2])
			if diff in table and diff > array[idx2]:
				triplet = [array[idx1], array[idx2], diff]
				tripletSums.append(triplet)
	return tripletSums

# ================================================================================================

# AlgoExpert solution 1: O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return triplets