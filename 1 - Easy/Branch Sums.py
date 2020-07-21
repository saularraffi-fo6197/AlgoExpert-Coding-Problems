# My attempt: O(n) time | O(n) space
# space complexity comes from storing sums in the array, and the length
#   of the array is equal to the number of leaf nodes, and the number of 
#   leaf nodes of a balances BST is roughly half of the number of nodes, 
#   so space complexity is O(n/s) which is really O(n)
def branchSumsHelper(root, sum, sumsArray):
	if root:
		sum = sum + root.value
        # first go down the left branches
		branchSumsHelper(root.left, sum, sumsArray)
		branchSumsHelper(root.right, sum, sumsArray)
        # onyl push sum to array if we are at the leaf node
		if root.left is None and root.right is None:
			sumsArray.append(sum)
    # return array when we are back at the root
	return sumsArray
		
def branchSums(root):
	return branchSumsHelper(root, 0, [])

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(n) space
def calculateBranchSums(node, runningSum, sums):
	# reached empty node
    if node is None:
		return
	
    # add current node value to running sum
	newRunningSum = runningSum + node.value
	
    # if we are at a child node, append the sum to the sums array
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	
    # first go left then go right
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)
		
def branchSums(root):
	sums = []
    # when you pass an array to a function in python, changes made to that array persist,
    #   which is why we can access the modified array after the function call
	calculateBranchSums(root, 0, sums)
	return sums





# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None