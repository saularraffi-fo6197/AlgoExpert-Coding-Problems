# My attempt: O(2^n) time | O(n) space
def getNthFib(n):
    if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n-1) + getNthFib(n-2)

# ================================================================================================

# My attempt: O(n) time | O(1) space
# where n is the parameter passed
def getNthFib(n):
	fib1, fib2 = 0, 1
	
	if n < 2: return n-1
	
    for i in range(n-2):
		tmp = fib1
		fib1 = fib2
		fib2 = tmp + fib2
	
	return fib2

# ================================================================================================

# # AlgoExpert solution 1: O(n) time | O(n) space
def getNthFib(n,cache={1: 0, 2: 1}):
    # if previously calculated fib number exists in our cache (dictionary obj),
    #   then look it up using key n (constant time) and return the value. This solves
    #   the problem from the more basic fib recursie function where there are a lot 
    #   of duplicate function calls
    if n in cache:
		return cache[n]
	else:
		cache[n] = getNthFib(n - 1, cache) + getNthFib(n - 2, cache)
		return cache[n]

    # time complexity is O(n) because we calculate fib num for every num 3-n and the rest
    #   of the numbers we lookup in our cache.
    