EXAMPLE = """
"""


def part1(inputdata: str) -> int:
    return len(inputdata.splitlines())


def part2(inputdata: str) -> int:
    return len(inputdata.splitlines())


def main():
    with open("input/NN.txt", "r", encoding="utf-8") as fp:
        inputdata = fp.read()

    assert part1(EXAMPLE) == 42
    print(f"Part 1: {part1(inputdata)}")

    assert part2(EXAMPLE) == 27
    print(f"Part 2: {part2(inputdata)}")


if __name__ == "__main__":
    main()
