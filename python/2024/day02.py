import io
from typing import IO


def part_one(file: IO) -> int:
    answer = 0
    for line in file:
        report = [int(x) for x in line.rstrip().split()]
        diff = get_differences(report)
        if safe_report(diff):
            answer += 1
    return answer


def part_two(file: IO) -> int:
    answer = 0
    for line in file:
        report = [int(x) for x in line.rstrip().split()]
        diff = get_differences(report)
        if safe_report(diff):
            answer += 1
            continue

        for i, _ in enumerate(report):
            new_report = report[:i] + report[i + 1 :]
            diff = get_differences(new_report)
            if safe_report(diff):
                answer += 1
                break
    return answer


def get_differences(report: list[int]) -> list[int]:
    return [report[x + 1] - report[x] for x in range(len(report) - 1)]


def safe_report(diff: list[int]) -> bool:
    return (all(x > 0 for x in diff) or all(x < 0 for x in diff)) and all(
        abs(x) >= 1 and abs(x) <= 3 for x in diff
    )


def main() -> None:
    example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    answer = part_one(io.StringIO(example))
    assert answer == 2

    file = open("input_day02.txt", "r", encoding="utf-8")
    answer = part_one(file)
    print(f"Part 1: {answer}")

    answer = part_two(io.StringIO(example))
    assert answer == 4

    file = open("input_day02.txt", "r", encoding="utf-8")
    answer = part_two(file)
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
