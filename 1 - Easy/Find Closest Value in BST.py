# My attempt: O(log(n)) time | O(1) space
def findClosestValueInBst(tree, target):
    # this algorithm is almost like search algorithm for BST, but rather than finding
    #   the value itself, we're just finding the closes value
	closestVal = tree.value
    # while the node we are on is not null
	while tree:
        # if value of node is closer to target than previously stored closest value
		if abs(target - tree.value) < abs(target - closestVal):
			closestVal = tree.value
		
        # go to left node if target is less than current node value, otherwise go right
		tree = tree.left if target < tree.value else tree.right
			
	return closestVal

# ================================================================================================
  
# My attempt 2: average - O(log(n)) time | O(log(n)) space
#               worst   - O(n) time | O(n) space --> BST that is basically a linked list
# space complexity is equal to time complexity (which here it is O(log(n))) because we are 
#   creating new frames on the call stack every time we call the recursive function
def findClosestValueInBstHelper(tree, target, closestVal):
	if not tree:
		return closestVal
	
    # go left
	if target < tree.value:
		if abs(target - tree.value) < abs(target - closestVal):
			return findClosestValueInBstHelper(tree.left, target, tree.value)
		else:
			return findClosestValueInBstHelper(tree.left, target, closestVal)
    # go right
	else:
		if abs(target - tree.value) < abs(target - closestVal):
			return findClosestValueInBstHelper(tree.right, target, tree.value)
		else:
			return findClosestValueInBstHelper(tree.right, target, closestVal)

def findClosestValueInBst(tree, target):	
	return findClosestValueInBstHelper(tree, target, tree.value)

# ================================================================================================

# AlgoExpert solution 1: average - O(log(n)) time | O(log(n)) space
#                        worst   - O(n) time | O(n) space --> BST that is basically a linked list
def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	
    # first determine the closest value. Either original closest value or tree.value
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	
    # going left
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
    # going right
	elif target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
    # found an exact match, break recursion and return this value
	else:
		return closest

def findClosestValueInBst(tree, target):	
	return findClosestValueInBstHelper(tree, target, tree.value)

# ================================================================================================

# AlgoExpert solution 2: average - O(log(n)) time | O(1) space
#                        worst   - O(n) time | O(1) space
def findClosestValueInBstHelper(tree, target, closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
        # difference between target and currentNode.value is 0 --> exit
		else:
			break
	return closest
	
def findClosestValueInBst(tree, target):	
	return findClosestValueInBstHelper(tree, target, tree.value)





# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None