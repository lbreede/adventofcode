# --- Day 2: Corruption Checksum ---

Spreadsheet = list[list[int]]


def parse_spreadsheet(filename: str) -> Spreadsheet:
    with open(filename, encoding="utf-8") as fp:
        return [[int(n) for n in line.split()] for line in fp.read().splitlines()]


def part_one(spreadsheet: Spreadsheet) -> int:
    return sum([max(row) - min(row) for row in spreadsheet])


def part_two(spreadsheet: Spreadsheet) -> int:
    checksum = 0
    for row in spreadsheet:
        for i, num in enumerate(row):
            quotients = [num // n for n in row[:i] + row[i + 1 :] if not num % n]
            checksum += quotients[0] if quotients else 0
    return checksum


def main() -> None:
    checksum = part_one(parse_spreadsheet("day02_example01.txt"))
    assert checksum == 18

    spreadsheet = parse_spreadsheet("day02_input.txt")
    checksum = part_one(spreadsheet)
    print("Part 1:", checksum)

    checksum = part_two(parse_spreadsheet("day02_example02.txt"))
    assert checksum == 9

    checksum = part_two(spreadsheet)
    print("Part 2:", checksum)


if __name__ == "__main__":
    main()
