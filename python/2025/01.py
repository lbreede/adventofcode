from operator import add, sub

EXAMPLE = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def part1(inputdata: str) -> int:
    password = 0
    dial = 50
    for line in inputdata.splitlines():
        op = add if line[0] == "R" else sub
        dial = op(dial, int(line[1:])) % 100
        password += int(dial == 0)
    return password


def part2(inputdata: str) -> int:
    password = 0
    dial = 50
    for line in inputdata.splitlines():
        op = add if line[0] == "R" else sub
        for _ in range(int(line[1:])):
            dial = op(dial, 1) % 100
            password += int(dial == 0)
    return password


def main():
    with open("input/01.txt", "r", encoding="utf-8") as fp:
        inputdata = fp.read()

    assert part1(EXAMPLE) == 3
    print(f"Part 1: {part1(inputdata)}")

    assert part2(EXAMPLE) == 6
    print(f"Part 2: {part2(inputdata)}")


if __name__ == "__main__":
    main()
