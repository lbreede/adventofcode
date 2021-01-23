def passportList(input):
	lineList = [line.rstrip("\n") for line in open(input)]
	oneLine = ""
	for L in lineList:
		
		if L != "":
			oneLine += L + " "
		else:
			oneLine += "-"

	passportList = oneLine.split("-")
	return passportList

def createDictList(pList):
	pDictList = []
	for p in pList:
		elem = p.split(" ")
		elem.pop()
		pDict = {}
		for e in elem:
			ee = e.split(":")
			pDict[ee[0]] = ee[1]
		pDictList.append(pDict)
	return pDictList

def countValidPassports(pDictList):
	valid = 0
	for d in pDictList:
		numElem = len(d)
		if numElem == 8:
			valid += 1
		elif numElem == 7:
			if "cid" not in d:
				valid += 1
	return valid


passportList = passportList("input.txt")
passportDictList = createDictList(passportList)
validPassports = countValidPassports(passportDictList)
print("The answer for part one is: " + str(validPassports) + " valid passports.")



