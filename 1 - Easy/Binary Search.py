# My attempt: O(log(n)) time | O(1) space
def binarySearch(array, target):
	left = 0
	right = len(array) - 1
	
	while left <= right:
		middle = (left + right) // 2  # // means divide and round down (instead of using int())
		if target == array[middle]:
			return middle
		elif target > array[middle]:
			left = middle + 1
		else:
			right = middle - 1
	return -1

# ================================================================================================

# My attempt: O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    return binarySearchTreeHelper(array, target, 0, len(array)-1)

def binarySearchTreeHelper(array, target, left, right):
	middle = (left + right) // 2
	
	if array[middle] == target:
		return middle
	elif left > right:
		return -1
	elif target > array[middle]:
		return binarySearchTreeHelper(array, target, middle + 1, right)
	else:
		return binarySearchTreeHelper(array, target, left, middle - 1)