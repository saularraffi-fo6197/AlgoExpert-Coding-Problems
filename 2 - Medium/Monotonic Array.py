# My Attempt 1: O(n) time | O(1) space
def isMonotonic(array):
	if len(array) < 3:
		return True
	
	for idx in range(1, len(array)):
        # if variable 'direction' hasn't been defined yet
		if "direction" not in locals():
			if array[idx] == array[idx - 1]:
				continue
			else:
				direction = 0 if array[idx] < array[idx - 1] else 1
		else:
			if direction == 0 and array[idx] > array[idx - 1]:
				return False
			if direction == 1 and array[idx] < array[idx - 1]:
				return False
	return True

# ================================================================================================

# My Attempt 2: O(n) time | O(1) space
def isMonotonic(array):
	if len(array) < 3:
		return True
	
    # direction 0 -> direction not yet determined and/or adjacent values equal up until now 
    # direction -1 -> array is non-increasing
    # direction 1 -> array is non-decreasing 
	direction = 0
	
	for idx in range(1, len(array)):
		if direction == 0:
			if array[idx] == array[idx - 1]:
				continue
			else:
				direction = -1 if array[idx] < array[idx - 1] else 1
		else:
			if direction == -1 and array[idx] > array[idx - 1]:
				return False
			if direction == 1 and array[idx] < array[idx - 1]:
				return False
	return True

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(1) space
def isMonotonic(array):
    if len(array) <= 2:
		return True
	
	direction = array[1] - array[0]
	
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i - 1]
			continue
		if breaksDirection(direction, array[i - 1], array[i]):
			return False
	
	return True

def breaksDirection(direction, previousInt, currentInt):
	difference = currentInt - previousInt
	if direction > 0:
		return difference < 0
	return difference > 0

# ================================================================================================

# AlgoExpert solution 2: O(n) time | O(1) space
def isMonotonic(array):
    isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1, len(array)):
		if array[i] < array[i - 1]:
			isNonDecreasing = False
		if array[i] > array[i - 1]:
			isNonIncreasing = False
			
	return isNonDecreasing or isNonIncreasing