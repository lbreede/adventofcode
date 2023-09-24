# --- Day 5: A Maze of Twisty Trampolines, All Alike ---

import time


def escape_maze(jump_offsets: list[int], part: int) -> int:
    if 1 >= part >= 2:
        raise ValueError("part must be either 1 or 2")

    pointer = steps = 0
    while 0 <= pointer < len(jump_offsets):
        jump = jump_offsets[pointer]
        jump_offsets[pointer] += 1 if part == 1 or jump < 3 else -1
        pointer += jump
        steps += 1

    return steps


def main() -> None:
    example = [0, 3, 0, 1, -3]
    assert escape_maze(example.copy(), part=1) == 5

    with open("day05_input.txt", encoding="utf-8") as fp:
        jump_offsets = [int(x) for x in fp]

    start = time.time()
    steps = escape_maze(jump_offsets.copy(), part=1)
    duration = time.time() - start
    print(f"Part 1: exit reached in {steps:,} steps after {duration:.3f} seconds.")

    assert escape_maze(example, part=2) == 10

    start = time.time()
    steps = escape_maze(jump_offsets, part=2)
    duration = time.time() - start
    print(f"Part 2: exit reached in {steps:,} steps after {duration:.3f} seconds.")


if __name__ == "__main__":
    main()
