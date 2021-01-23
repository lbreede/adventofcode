lineList = list()
with open("input.txt") as f:
 	for line in f:
		lineList.append(int(line))

for a in lineList:
	for b in lineList:
		if a + b == 2020:
			print("The first answer is: " + str(a * b))

for a in lineList:
	for b in lineList:
		for c in lineList:
			if a + b + c == 2020:
				print("The second answer is: " + str(a * b * c))