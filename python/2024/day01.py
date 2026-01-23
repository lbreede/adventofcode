import io
import os.path
import time
from functools import partial
from typing import IO, Callable
from utils import assert_eq, run as _run

DAY: str = "01"
INPUT_FILE = f"input/{DAY}.txt"

EXAMPLE: str = """3   4
4   3
2   5
1   3
3   9
3   3"""

run = partial(_run, INPUT_FILE, EXAMPLE, os.path.basename(__file__))


def part1(reader: IO) -> int:
    m = [[int(x) for x in line.rstrip().split()] for line in reader]
    t = list(zip(*m))
    s = [sorted(row) for row in t]
    return sum(abs(b - a) for a, b in zip(s[0], s[1]))


def part2(reader: IO) -> int:
    m = [[int(x) for x in line.rstrip().split()] for line in reader]
    t = list(zip(*m))
    return sum(x * t[1].count(x) for x in t[0])


def main(print_day: bool = True):
    if print_day:
        print(f"\n== Day {DAY} ==")
    print("=== Part 1 ===")
    run(part1, 11)

    print("\n=== Part 2 ===")
    run(part2, 31)


if __name__ == "__main__":
    main(print_day=False)
