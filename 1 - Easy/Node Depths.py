# My attempt: O(n) time | O(h) space -> where h is the height of the tree
def nodeDepths(root):
    return nodeDepthsHelper(root, 0)

def nodeDepthsHelper(root, depth):
	if root is None:
		return 0
	
    # if we are at a leaf node, return the depth of the node
	if root.left is None and root.right is None:
		return depth 
	
	else:
        # add current node depth to left and right node depth sums
        # increment depth when passing to function
		return depth + nodeDepthsHelper(root.left, depth+1) + nodeDepthsHelper(root.right, depth+1)

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(h) space -> where h is the height of the tree
def nodeDepths(root, depth=0):
    if root is None:
		return 0
	
	return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)





# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None