import os.path
from functools import partial
from typing import IO
from utils import run as _run

DAY: str = "NN"  # TODO: Fill the day
INPUT_FILE = f"input/{DAY}.txt"

EXAMPLE: str = """EXAMPLE INPUT
"""  # TODO: Add the test input

run = partial(_run, INPUT_FILE, EXAMPLE, os.path.basename(__file__))


def part1(reader: IO) -> int:
    # TODO: Solve Part 1 of the puzzle
    return -1


def part2(reader: IO) -> int:
    return -1


def main(print_day: bool = True):
    if print_day:
        print(f"\n== Day {DAY} ==")
    print("=== Part 1 ===")
    # TODO: Set the expected answer for the test input
    run(part1, 0)

    print("\n=== Part 2 ===")
    run(part2, 0)


if __name__ == "__main__":
    main(print_day=False)
