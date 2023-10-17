def processString(input_str):
	output_str = ""
	for char in input_str:
		if char.isupper():
			output_str += char.lower()
		elif char.isnumeric():
			output_str += char * 2
		else:
			output_str += char.upper()

	return output_str

def splitString(input_str, partCount):
	# Invalid partition count
	if (partCount > len(input_str)):
		return
	
	# Split the input into 4 equal parts of strings
	parts = []
	strLen = len(input_str)
	avgLen = strLen // partCount

	# Put together parts of the string
	for i in range(0, strLen, avgLen):
		part = input_str[i:i + avgLen]
		parts.append(part)
	
	return parts

def hasBug(input_str):
	correctOutput = ""
	for char in input_str:
		if char.isupper():
			correctOutput += char.lower()
		elif char.islower():
			correctOutput += char.upper()
		else:
			correctOutput += char 

	return correctOutput != processString(input_str)

def deltaDebug(input_str, partitions, testFunc):
	# Collects part of input that causes bugs
	buggyParts = []
	parts =  splitString(input_str, partitions) # Split the input

	# Find parts of input that cause bugs
	for part in parts:
		if testFunc(part):
			buggyParts.append(part)

	# Return these buggy parts
	return buggyParts

tests = [
	"abcdefG1",
	"CCDDEExy",
	"1234567b",
	"8665"
]

for test in tests:
	print("For", test)
	print( deltaDebug(test, 4, hasBug) )
	