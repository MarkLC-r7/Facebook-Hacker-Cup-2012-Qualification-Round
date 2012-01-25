import sys, math
from collections import Counter

if len(sys.argv) < 2:
	print "Usage: python alphabet_soup.py inputFilename"
	exit(0)

inputFile = open(sys.argv[1])
outputFile = open("output.txt", "w")

cases = inputFile.readlines()

for case in range(1,int(cases[0])+1):
	count = Counter(cases[case])
	count['C'] = int(math.floor(count['C'] / 2))

	newList = []
	for letter in "HACKERUP":
		newList.append(count[letter])
	minimum = min(newList)

	outputFile.write("Case #%d: %d\n"%(case, minimum))
		
inputFile.close()
outputFile.close()
