# --- Day 4: Security Through Obscurity ---

with open("input.txt", "r") as f:
	linelist = f.read().split("\n")

real_rooms = []



for line in linelist:

	parts = line.split("-")
	name = "".join(parts[:-1])
	sector_id, checksum = parts[-1].split("[")
	sector_id = int(sector_id)
	checksum = checksum[:-1]

	prev_count = float("inf")
	i = 0

	prev_letter = ""

	for letter in checksum:
		count = name.count(letter)

		if count < prev_count:
			print(letter)
			i += 1
		elif count == prev_count and letter == max(letter, prev_letter):

			print(letter)

			i += 1

		prev_count = count
		prev_letter = letter

	if i == 5:
		real_rooms.append(sector_id)

print(real_rooms)
print(sum(real_rooms))