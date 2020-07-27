# My attempt: 
#   Best:       O(n) time | O(1) space
#   Average:    O(n^2) time | O(1) space
#   Worst:      O(n^2) time | O(1) space
def bubbleSort(array):
    # iterate through whole array
    for i in range(len(array)):
        # iterate through whole array (minus last elem) until array[j] < array[j+1]
		for j in range(len(array)-1):
            # swap array[j] and array[j+1]
			if array[j] > array[j+1]:
				tmp = array[j]
				array[j] = array[j+1]
				array[j+1] = tmp
	return array

# ================================================================================================

# AlgoExpert solution 1: 
#   Best:       O(n) time | O(1) space
#   Average:    O(n^2) time | O(1) space
#   Worst:      O(n^2) time | O(1) space
def bubbleSort(array):
    isSorted = False
	counter = 0
	while not isSorted:
		isSorted = True
        # counter is used so that we don't iterate through the sorted end of the array,
        #   we are always iterating from index 0 to (end - counter)
		for i in range(len(array) - 1 - counter):
            # if no elements are out of place, if statement will never trigger and 
            #   isSorted will never change from True to False
			if array[i] > array[i + 1]:
				swap(i, i + 1, array)
				isSorted = False
		counter += 1
	return array

def swap(i, j, array):
    # cool way to swap array elements without temp value
	array[i], array[j] = array[j], array[i]