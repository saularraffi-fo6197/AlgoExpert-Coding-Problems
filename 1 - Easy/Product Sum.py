# My Attempt: O(n) time | O(d) space
# 	Where n is the total number of elements (including elements in sub-arrays) and
# 	d is the depth of the arrays
from math import factorial
def productSum(array, depth=1):
	sum = 0
	for element in array:
		if type(element) is not list:
			sum = sum + element
		else:
			sum = sum + productSum(element, depth + 1)
	return sum * depth










# iterative approach using stacks (does not work yet)
# ===================================================
def productSum(array):
	sumStack = []
	indexStack = [0]
	
    while len(indexStack) > 0:
		index = lastElem(indexStack)
		print(index)
		
		if index >= len(array):
			indexStack.pop()
			sumStack[-1:] = lastElem(sumStack) + (sumStack.pop() * len(sumStack))
			
		elif type(array[index]) is not list:
			sumStack[-1:] = lastElem(sumStack) + array[index]
		else:
			sumStack.append(array[index])
			indexStack.append(0)
			
		indexStack[-1:] = lastElem(indexStack) + 1

def lastElem(array):
	return array[-1:][0]