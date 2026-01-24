import time
from aoc_helper import read_input_to_string, start_day

DAY = 3
EXAMPLE = """987654321111111
811111111111119
234234234234278
818181911112111"""


def max_k_subseq(digits: str, k: int) -> int:
    to_remove = len(digits) - k
    stack = []
    for d in digits:
        while to_remove and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)
    return int("".join(stack[:k]))


def part1(inputdata: str) -> int:
    return sum(max_k_subseq(bank, 2) for bank in inputdata.splitlines())


def part2(inputdata: str) -> int:
    return sum(max_k_subseq(bank, 12) for bank in inputdata.splitlines())


def main():
    start_day(DAY)
    inputdata = read_input_to_string(DAY)

    assert part1(EXAMPLE) == 357
    start = time.time()
    result = part1(inputdata)
    elapsed = time.time() - start
    print(f"Part 1: {result}, took {elapsed:.3f}s")

    assert part2(EXAMPLE) == 3121910778619
    start = time.time()
    result = part2(inputdata)
    elapsed = time.time() - start
    print(f"Part 2: {result}, took {elapsed:.3f}s")


if __name__ == "__main__":
    main()
