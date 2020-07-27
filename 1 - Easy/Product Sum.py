def productSum(array, index=0, depth=1):
	if index > len(array) - 1:
		return 0
	else:
		return (array[index] * depth) + productSum(array, index+1)


def productSum(array, index=0, depth=1):
	if index > len(array) - 1:
		return 0
	else:
		print(array[index])
		if type(array[index]) != list:
			return (array[index] * depth) + productSum(array, index+1, depth)
		else:
			return productSum(array[index], 0, depth+1)

def productSum(array, depth=1, sum=0):
	for elem in array:
		if type(elem) == list:
			sum = productSum(elem, depth+1, sum)
		else:
			sum = sum + (elem * depth)
			print(elem, " * ", depth, ", sum = ", sum)
	return sum

def productSum(array, index=0, depth=1, sum=0):
	if index > len(array) - 1:
		return 0
	else:
		if type(array[index]) == list:
			return productSum(array[index], 0, depth+1, 0)
		else:
			print(array[index])
			sum = sum + array[index] + productSum(array, index+1, 1, sum)
			return sum

# remember order of operations
# ====================================================


# iterative approach using stacks
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