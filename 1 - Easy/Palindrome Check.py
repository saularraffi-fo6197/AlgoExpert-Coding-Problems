# My Attempt: O(n) time | O(1) space
def isPalindrome(string):
    # keep track of left and right indices 
    left = 0
	right = len(string) - 1
    # loop until left index goes past right index
	while left <= right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True

# ================================================================================================

# My Attempt: O(n) time | O(1) space
from math import ceil
def isPalindrome(string):
    # iterate through half of the string characters
    for i in range(ceil(len(string)/2)):
        # compare string character to mirror side string character
		if string[i] != string[len(string) - i - 1]:
			return False
	return True

# ================================================================================================

# AlgoExpert solution 1: O(n^2) time | O(n) space
def isPalindrome(string):
    # just check if the string is the same as the string reversed
    reversedString = ""
    # reversed() reverses the order of the array: [1,2,3,4] --> [4,3,2,1]
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string == reversedString
# ================================================================================================

# AlgoExpert solution 2: O(n) time | O(n) space
def isPalindrome(string):
    reversedChars = []
	for i in reversed(range(len(string))):
		reversedChars.append(string[i])
	return string == "".join(reversedChars)

# ================================================================================================

# AlgoExpert solution 3: O(n) time | O(n) space
def isPalindrome(string):
    j = len(string) - 1 - i
	return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)