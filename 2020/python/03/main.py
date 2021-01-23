def slopeCheck(input, hori, vert):
	lineList = [line.rstrip("\n") for line in open(input)]
	pos = 0
	found = 0
	i = 0
	for line in lineList:
		if i % vert == 0:
			if line[pos % len(line)] == "#":
				found += 1
			pos += hori
		i += 1
	return found

a = slopeCheck("input.txt", 1, 1)
b = slopeCheck("input.txt", 3, 1)
c = slopeCheck("input.txt", 5, 1)
d = slopeCheck("input.txt", 7, 1)
e = slopeCheck("input.txt", 1, 2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(a*b*c*d*e)