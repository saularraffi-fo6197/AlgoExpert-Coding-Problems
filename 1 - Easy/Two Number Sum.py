# My attempt
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		for j in range(len(array)):
			if (array[i] != array[j] and array[i] + array[j] == targetSum):
				return [array[i], array[j]]
	return []

# ================================================================================================

# AlgoExpert solution 1: O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    # no need to visit the last element because secondNum is always the element after
    #   first num. If firstNum is the last element, there's nothing after it to compare with
	for i in range(len(array) - 1):
		firstNum = array[i]
        # no need to compare secondNum to any elements before it because they have already
        #   been compared
		for j in range(i + 1, len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
	return []

# ================================================================================================

# AlgoExpert solution 2: O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    # this dictionary is our hash table (lookup time complexity of O(1))
	nums = {}
	for num in array:
        # by subtracting targetSum by element in array, you've got a potential second num
        # x + y = target --> x = target - y --> is x in array?
		potentialMatch = targetSum - num
        # then you just have to lookup potentialMatch (or x) in hash table
		if potentialMatch in nums:
			return [potentialMatch, num]
		else:
            # store num in hash table with value of True signifying that it is present in array
			nums[num] = True
	return []

    # space complexity is O(n) because at worst we will store every element in the hash table

# ================================================================================================

# AlgoExpert solution 3: O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
    # start with pointers at both ends of the array
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			return [array[left], array[right]]
        # if sum is less than target, move left pointer to the right,
        #   therefore working with larger number 
		elif currentSum < targetSum:
			left += 1
        # if sum is more than target, move right pointer to the left,
        #   therefore working with smaller number 
		elif currentSum > targetSum:
			right -= 1
	return []

    # the sorting algorithm had the highest time complexity, therefore the
    #   O(nlog(n)) time complexity comes from sorting

