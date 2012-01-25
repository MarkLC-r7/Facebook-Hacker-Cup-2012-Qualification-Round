import sys

if len(sys.argv) < 2:
	print "Usage: python script.py input_filename"
	exit(0)

inputFile = open(sys.argv[1])
outputFile = open("output.txt", "w")

N = int(inputFile.readline())

def check_fit(words, font, billWidth, billHeight):

	sentence = " ".join(words)
	total_width = len(sentence) * font

	if total_width <= billWidth:
		if font <= billHeight:
			return True
		else:
			return False 

	i = 0
	j = 1
	lines = 0
	while True:
		if j > len(words):
			lines += 1
			break
		temp = " ".join(words[i:j])
		tempWidth = len(temp) * font

		if i == j - 1 and tempWidth > billWidth:
			return False

		if tempWidth < billWidth:
			j += 1
			continue
		if tempWidth == billWidth:
			lines += 1
			i = j
			j = i + 1
			continue
		if tempWidth > billWidth:
			if i == 0 and j == 1:
				return False
			i = j - 1
			lines += 1
			continue

	height = lines * font

	if height <= billHeight:
		return True
	else:
		return False
	
for case in range(1,N+1):
	params = inputFile.readline().split()
	width = int(params[0])
	height = int(params[1])
	
	words = []
	for par in range(2,len(params)):
		words.append(params[par])

	sentence = " ".join(words)
	font = 1

	while True:
		if check_fit(words,font, width, height) == True:
			font += 1
		else:
			font -= 1
			break
		
	outputFile.write("Case #%d: %d\n" %(case, font))
	
inputFile.close()
outputFile.close()
