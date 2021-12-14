# --- Day 8: Handheld Halting ---

from aoc_helper import load_input
linelist = load_input("day08_example.txt")

def process_data(lst):
	oplist = []
	for i, line in enumerate(lst):
		op, arg = line.split()
		arg = int(arg)
		oplist.append([i, op, arg])
	return oplist

def run_program(lst):
	value = 0
	i = 0
	id_list = []

	while True:		
		id_, op, arg = lst[i]
		if id_ not in id_list:
			if op == "acc":
				value += arg
				i += 1
			elif op == "jmp": i += arg
			elif op == "nop": i += 1
			id_list.append(id_)
		else:
			return value
			break

oplist = process_data(linelist)
value = run_program(oplist)

n = sum(x.count("nop") for x in oplist) + sum(x.count("jmp") for x in oplist)

for i in range(n):
	print(i)
