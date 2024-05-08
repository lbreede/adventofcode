# --- Day 1: Inverse Captcha ---
import time
from typing import Callable


def part_one(captcha: str) -> int:
    return solve_captcha(captcha, lambda i, length: captcha[(i + 1) % length])


def part_two(captcha: str) -> int:
    return solve_captcha(captcha, lambda i, length: captcha[(i + length // 2) % length])


def solve_captcha(captcha: str, func: Callable[[int, int], str]) -> int:
    length = len(captcha)
    solution = 0
    for i, a in enumerate(captcha):
        b = func(i, length)
        if a == b:
            solution += int(a)
    return solution


def main():
    assert part_one("1122") == 3
    assert part_one("1111") == 4
    assert part_one("1234") == 0
    assert part_one("91212129") == 9

    with open("day01_input.txt", encoding="utf-8") as fp:
        captcha = fp.read().strip()

    start = time.time()
    solution = part_one(captcha)
    duration = time.time() - start
    print(f"Part 1: {solution:,} after {duration:.3f} seconds.")

    assert part_two("1212") == 6
    assert part_two("1221") == 0
    assert part_two("123425") == 4
    assert part_two("123123") == 12
    assert part_two("12131415") == 4

    start = time.time()
    solution = part_two(captcha)
    duration = time.time() - start
    print(f"Part 2: {solution:,} after {duration:.3f} seconds.")


if __name__ == "__main__":
    main()
