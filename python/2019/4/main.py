# --- Day 4: Secure Container ---

PUZZLE_INPUT = "137683-596253"

def criteria1(password):
	if len(str(password)) == 6:
		return True
	else:
		return False

def criteria2(password, puzzle_input):
	min_, max_ = [int(x) for x in puzzle_input.split("-")]
	if password >= min_ and password <= max_:
		return True
	else:
		return False

def criteria3(password):
	DOUBLES = {"00", "11", "22", "33", "44", "55", "66", "77", "88", "99"}
	for d in DOUBLES:
		if d in str(password):
			return True
			break

def criteria4(password):
	a,b,c,d,e,f = [int(x) for x in str(password)]

	if a <= b and b <= c and c <= d and d <= e and e <= f:
		return True
	else:
		return False

pw = 111111
c1 = criteria1(pw)
# c2 = criteria2(pw, PUZZLE_INPUT)
c3 = criteria3(pw)
c4 = criteria4(pw)

start, end = [int(x) for x in PUZZLE_INPUT.split("-")]

match = 0
for x in range(start, end+1):
	c1 = criteria1(x)
	c3 = criteria3(x)
	c4 = criteria4(x)
	if c1 and c3 and c4:
		match += 1

print(match)




