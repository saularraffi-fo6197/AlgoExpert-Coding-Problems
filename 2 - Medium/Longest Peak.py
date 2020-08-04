def longestPeak(array):
    longestPeak = 0
	localPeakLength = 0
	inPeak, goingUp = False, False
	
	for idx in range(1, len(array)):		
		if inPeak:
			if goingUp:
				if array[idx] > array[idx - 1]:
					localPeakLength = localPeakLength + 1
				else:
					goingUp = False
			else:
				if array[idx] < array[idx - 1]:
					localPeakLength = localPeakLength + 1
				else:
					inPeak = False
		else:
			
			longestPeak = localPeakLength if localPeakLength > longestPeak else longestPeak
			
			if array[idx] > array[idx - 1]:
				inPeak, goingUp = True, True
	
	return longestPeak






def longestPeak(array):
    longestPeak = 0
	localPeakLength = 0
	inPeak = False
	
	for idx in range(1, len(array)):
		if inPeak:
			localPeakLength += 1
			if array[idx] == array[idx - 1]:
				inPeak = False
				localPeakLength = 0
			elif (idx+1) < len(array) and array[idx] > array[idx - 1] and array[idx] < array[idx + 1]:
				longestPeak = localPeakLength if localPeakLength > longestPeak else longestPeak
				inPeak = False
		else:
			if array[idx] > array[idx - 1]:
				localPeakLength = 1
				inPeak = True
		
		print(array[idx], longestPeak, localPeakLength)
	
	return longestPeak
