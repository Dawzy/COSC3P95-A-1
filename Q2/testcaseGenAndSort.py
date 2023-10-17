import random

testCasesCount = 10
maxLength = 10
minValue = -999
maxValue = 999

def generateTestCases():
	# Configure test case data
	testCasesCount = int(input("Num of testcases: "))
	minLength = 0
	maxLength = int(input("Max Array Length: "))
	minValue = int(input("Min Int Value: "))
	maxValue = int(input("Max Int Value: "))

	testcases = []
	
	# Generate test cases
	for i in range(testCasesCount):
		testcase = []
		testcaseLen = random.randrange(minLength, maxLength) # Test case length

		# Construct test case
		for j in range(testcaseLen):
			testcase.append(random.randrange(minValue, maxValue))
		
		testcases.append(testcase)

	return testcases

# Basic bubble sort
def bubbleSort(array):
	# Iterate through array comparing two elements at a time
	# Swap them if the smaller element comes after the bigger one
	for i in range( len(array) ):
		for j in range( len(array) - i - 1 ):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
	return array


# Check if the array is sorted in ascending order
def isAscending(array):
	for i in range( len(array) - 1 ):
		if array[i] > array[i+1]:
			return False
	return True

testcases = generateTestCases()
for case in testcases:
	sortedCase = bubbleSort(case)
	print("Testcase:", case)
	print("Sorted:", sortedCase)
	print("Passed:", isAscending(sortedCase))
	print("------------------")
