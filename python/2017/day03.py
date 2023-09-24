# --- Day 3: Spiral Memory ---

from math import sqrt, ceil
from time import time
from typing import Optional


def part_one(num: int) -> int:
    spiral_size = ceil(sqrt(num))
    spiral_size = spiral_size if spiral_size % 2 else spiral_size + 1
    largest_corner = spiral_size**2
    spiral_size -= 1
    corners = [largest_corner - spiral_size * i for i in range(5)]
    dist_to_corner = min([abs(num - i) for i in corners])
    return spiral_size - dist_to_corner


def part_two(num: int) -> Optional[int]:
    with open("b141481.txt", encoding="utf-8") as fp:
        for line in fp:
            if line.startswith("#"):
                continue
            val = int(line.split()[1])
            if val > num:
                return val
    return None


def main() -> None:
    assert part_one(1) == 0
    assert part_one(12) == 3
    assert part_one(23) == 2
    assert part_one(1024) == 31
    assert part_one(10) == 3
    assert part_one(24) == 3

    puzzle_input = 368_078
    start = time()
    dist = part_one(puzzle_input)
    duration = time() - start
    print(f"Part 1: {dist} ({duration:.3f}s)")

    start = time()
    solution = part_two(puzzle_input)
    duration = time() - start
    print(f"Part 2: {solution:,} ({duration:.3f}s)")


if __name__ == "__main__":
    main()
