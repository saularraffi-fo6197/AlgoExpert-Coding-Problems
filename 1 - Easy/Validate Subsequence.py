# My attempt: O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    i = 0 
	end = len(sequence) - 1
	for num in array:
		if (num == sequence[i]):
			if (i == end):
				return True
			i = i + 1
	return False

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
        # every time we have a match, increase seqIdx
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
    # if all sequence elements were matched, then the seqIdx should be 
    #   equal to the length of the sequence array
	return seqIdx == len(sequence)

# AlgoExpert solution 2: O(n) time | O(1) space
def isValidSubsequence(array, sequence):
	seqIdx = 0
	for value in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == value:
			seqIdx += 1
	return seqIdx == len(sequence)