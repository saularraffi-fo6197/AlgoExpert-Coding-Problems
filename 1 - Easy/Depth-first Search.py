# My attempt: O(v + e) time | O(v) space
# where x = vertices (nodes) and e = edges (connections between 2 nodes)
# O(v) space complexity because of the array that we are storing and also
#   because of the frames we put on the call stack with every call to our 
#   recursive function. Worst case, our tree is one long linked list, so 
#   the number of frames will equal number of node/verticies
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # the first thing to do is append the current node value to the array
		array.append(self.name)
        # if the node has no children, then return
        if len(self.children) == 0:
			return
		else:
            # iterate through the child nodes from left to right
			for node in self.children:
                # change the value of self to the child node
                # this isn't necessary because you could have just called child.depthFirstSearch(array)
				self = node
				self.depthFirstSearch(array)
		return array

# ================================================================================================

# AlgoExpert solution 1: O(v + e) time | O(v) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
		array.append(self.name)
        # no need for a base case
		for child in self.children:
			child.depthFirstSearch(array)
		return array
				
				