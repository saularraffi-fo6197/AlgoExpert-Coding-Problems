# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
		if value < self.left:
			if self.left is not None:
				insert(self.left, value)
			else:
				self.left = BST(value)
		else:
			if self.right is not None:
				insert(self.right, value)
			else:
				self.right = BST(value)
        return self

    def contains(self, value):
        if self.left is None and self.right is None:
			return False
		elif self.value == value:
			return True
		else:
			if value < self.value:
				return contains(self.left, value)
			else:
				return contains(self.right, value)

    def remove(self, value):
        pass
