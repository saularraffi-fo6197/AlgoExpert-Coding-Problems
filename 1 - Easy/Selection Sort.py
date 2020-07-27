# My attempt: 
#   Best:       O(n^2) time | O(1) space
#   Average:    O(n^2) time | O(1) space
#   Worst:      O(n^2) time | O(1) space
def selectionSort(array):
	for idx in range(len(array)):
		minIdx = idx
		# traverse the array from idx to end to find index of min value
		for j in range(idx + 1,len(array)):
			if array[j] < array[minIdx]:
				minIdx = j
		# once correct min value index is found, swap it with the value at index idx
		array[idx], array[minIdx] = array[minIdx], array[idx]
	return array