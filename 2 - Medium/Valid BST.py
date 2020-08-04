# My Attempt 1: O(n) time | O(d) space 
#   where d is the depth of the tree		
def validateBst(tree, rightParent=float("inf"), leftParent=float("-inf")):
	if tree is None:
		return True
	elif tree.value >= rightParent or tree.value < leftParent:
		return False
	else:
		return validateBst(tree.left, tree.value, leftParent) and validateBst(tree.right, rightParent, tree.value)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(d) space
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue:
		return False
	leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
	return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)