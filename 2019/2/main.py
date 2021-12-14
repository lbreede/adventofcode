# --- Day 2: 1202 Program Alarm ---

with open("input.txt", "r") as fp:
	raw_program = fp.read()

# raw_program = "1,1,1,4,99,5,6,0,99"
program = [int(x) for x in raw_program.split(",")]

def run_program(program, noun, verb):

	new_program = program[:]

	new_program[1] = noun
	new_program[2] = verb

	i = 0

	while True:
		opcode = new_program[i]

		if opcode == 99:
			break
		elif opcode == 1 or opcode == 2:
			idx1 = new_program[i+1]
			idx2 = new_program[i+2]
			idx3 = new_program[i+3]

			val1 = new_program[idx1]
			val2 = new_program[idx2]

			if opcode == 1:
				result = val1 + val2
			elif opcode == 2:
				result = val1 * val2
			else:
				raise ValueError("Bad opcode!")

			new_program[idx3] = result

		else:
			raise ValueError("Bad opcode!")

		i += 4

	return new_program[0]

print(f"Part 1: {run_program(program, 12, 2)}")

for i in range(100):
	for j in range(100):
		result = run_program(program, i, j)
		if result == 19690720:
			print(f"Part 2: {100 * i + j}")
			break