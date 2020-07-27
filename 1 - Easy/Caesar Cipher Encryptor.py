# My Attempt: O(n) time | O(n) space
from math import ceil
def caesarCipherEncryptor(string, key):
    newString = ""
	for letter in string:
		newString = newString + getNewLetter(letter,key)
	return newString

def getNewLetter(letter, key):
	newCharNum = ord(letter) + key
	if newCharNum > 122:
		# how many times do we need to wrap around? (26 letters in alphabet)
		multiplier = ceil((newCharNum - 122) / 26)
		# wrap around
		newCharNum = newCharNum + (96 - 122) * multiplier
	return chr(newCharNum)

# ================================================================================================

# My Attempt: O(n) time | O(n) space
from math import ceil
def caesarCipherEncryptor(string, key):
    newString = ""
	for letter in string:
		newString = newString + getNewLetter(letter,key)
	return newString

def getNewLetter(letter, key):
	newCharNum = ord(letter) + key
	# wrap around as many times as needed using the remainder operator 
	newCharNum = ((newCharNum - 96) % 26) + 96
	# when newCharNum is 122, it wraps around even though it shouldn't, haven't found a fix yet
	return "z" if newCharNum == 96 else chr(newCharNum)

# ================================================================================================

# AlgoExpert solution 1: O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
	# He mods the key, wheras we modded the resulting numeric value of the char, but his way is
	# 	a lot smarter
	newKey = key % 26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# ================================================================================================

# AlgoExpert solution 2: O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
	newKey = key % 26
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey, alphabet))
	return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
	newLetterCode = alphabet.index(letter) + key
	return alphabet[newLetterCode % 26]