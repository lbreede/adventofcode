import os.path
from functools import partial
from typing import IO
from utils import run as _run

DAY: str = "02"
INPUT_FILE = f"input/{DAY}.txt"

EXAMPLE: str = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

run = partial(_run, INPUT_FILE, EXAMPLE, os.path.basename(__file__))


def part1(reader: IO) -> int:
    answer = 0
    for line in reader:
        report = [int(x) for x in line.rstrip().split()]
        answer += safe_report(report)
    return answer


def part2(reader: IO) -> int:
    answer = 0
    for line in reader:
        report = [int(x) for x in line.rstrip().split()]
        if safe_report(report):
            answer += 1
            continue
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1 :]
            if safe_report(new_report):
                answer += 1
                break

    return answer


def safe_report(report: list[int]) -> bool:
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return (all(x > 0 for x in diffs) or all(x < 0 for x in diffs)) and all(
        1 <= abs(x) <= 3 for x in diffs
    )


def main(print_day: bool = True):
    if print_day:
        print(f"\n== Day {DAY} ==")

    print("=== Part 1 ===")
    run(part1, 2)

    print("\n=== Part 2 ===")
    run(part2, 4)


if __name__ == "__main__":
    main(print_day=False)
