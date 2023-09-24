# --- Day 1: Inverse Captcha ---

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
    solution = part_one("1122")
    assert solution == 3

    solution = part_one("1111")
    assert solution == 4

    solution = part_one("1234")
    assert solution == 0

    solution = part_one("91212129")
    assert solution == 9

    with open("day01_input.txt", encoding="utf-8") as fp:
        captcha = fp.read().strip()
    solution = part_one(captcha)
    print("Part 1:", solution)

    solution = part_two("1212")
    assert solution == 6

    solution = part_two("1221")
    assert solution == 0

    solution = part_two("123425")
    assert solution == 4

    solution = part_two("123123")
    assert solution == 12

    solution = part_two("12131415")
    assert solution == 4

    solution = part_two(captcha)
    print("Part 2:", solution)


if __name__ == "__main__":
    main()
