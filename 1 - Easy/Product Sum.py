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