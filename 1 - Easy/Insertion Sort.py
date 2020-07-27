# My attempt: 
#   Best:       O(n) time | O(1) space
#   Average:    O(n^2) time | O(1) space
#   Worst:      O(n^2) time | O(1) space
def insertionSort(array):
    # idxSorted keeps track of the last index of the sorted sub-array
	for idxSorted in range(len(array) - 1):
        # idx corresponds to the value we are going to insert in the sorted sub-array 
		idx = idxSorted + 1
		while idx > 0:
            # keep swapping array[idx] and the element on its left until array[idx] is in correct position
			if array[idx] < array[idx-1]:
				array[idx], array[idx-1] = array[idx-1], array[idx]
				idx = idx - 1
			else:
				 break
	return array

# ================================================================================================

# AlgoExpert solution 1: 
#   Best:       O(n) time | O(1) space
#   Average:    O(n^2) time | O(1) space
#   Worst:      O(n^2) time | O(1) space
def insertionSort(array):
	for i in range(1, len(array)):
		j = i
        # keep swapping unsorted element with the element to its left until unsorted element is
        #   greater than element to its left or until it is the first element (j == 0)
		while j > 0 and array[j] < array[j - 1]:
			swap (j, j - 1, array)
			j -= 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]