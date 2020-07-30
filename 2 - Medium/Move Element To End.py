# My Attempt 1: O(n^2) time | O(n) space
#   I'm pretty sure time is O(n^2) because the pop() method is worst caes O(n)
#   O(n) space because we are adding to the openPositions array for every instance of toMove
#       and there could be n instances, where n is the length of the array
def moveElementToEnd(array, toMove):
    occurrences = 0
    # initializing queue to store open positions
	openPositions = []
	for idx in range(len(array)):
		if array[idx] == toMove:
			occurrences += 1
            # queue in
			openPositions.append(idx)
		else:
			if len(openPositions) > 0:
                # queue out
				array[openPositions.pop(0)] = array[idx]
				openPositions.append(idx)
	
    # filling the last x positions with toMove, where x is the number of occurrences of toMove
	for idx in reversed(range(len(array))):
		if occurrences != 0:
			array[idx] = toMove
			occurrences -= 1
		else:
			break
	
	return array

# ================================================================================================

# My Attempt 2: O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    left = 0
	right = len(array) - 1
	while left < right:
		if array[right] == toMove:
			right -= 1
			continue
		elif array[left] != toMove:
			left += 1
			continue
		# if array[left] == toMove
		else:
			array[left], array[right] = array[right], array[left]
			left += 1
			right -= 1
	
	return array

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    i = 0
	j = len(array) - 1
	while i < j:
		while i < j and array[j] == toMove:
			j -= 1
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i]
		i += 1
	return array