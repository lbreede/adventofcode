# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

f = open("input.txt", "r").read()

x = 0
y = 0
start = [x, y]
positions = [start]

for c in f:
	pos = []
	if c == "^":
		y += 1
	elif c == "v":
		y -= 1
	elif c == ">":
		x += 1
	elif c == "<":
		x -= 1
	pos = [x, y]
	positions.append(pos)

uniquePositions = set(tuple(i) for i in positions)

print(len(uniquePositions))	