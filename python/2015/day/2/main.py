# --- Day 2: I Was Told There Would Be No Math ---


paper = ribbons = 0
with open("input.txt", "r", encoding="utf-8") as fp:
    for line in fp:
        length, width, height = [int(dim) for dim in line.rstrip().split("x")]
        paper += (
            2 * length * width
            + 2 * width * height
            + 2 * height * length
            + min(length * width, width * height, height * length)
        )
        ribbons += (
            sum(sorted((length, width, height))[:2]) * 2 + length * height * width
        )
print("Part 1:", paper, "\nPart 2:", ribbons)
