# --- Day 5: A Maze of Twisty Trampolines, All Alike ---

import time


def escape_maze(offsets: list[int], part_two: bool = False) -> int:
    pointer = steps = 0
    while 0 <= pointer < len(offsets):
        offset = offsets[pointer]
        offsets[pointer] += 1 if not part_two or offset < 3 else -1
        pointer += offset
        steps += 1
    return steps


def main() -> None:
    example = [0, 3, 0, 1, -3]
    assert escape_maze(example.copy()) == 5

    with open("day05_input.txt", encoding="utf-8") as fp:
        jump_offsets = [int(x) for x in fp]

    start = time.time()
    steps = escape_maze(jump_offsets.copy())
    duration = time.time() - start
    print(
        f"Part 1: exit reached in {steps:,} steps after {duration:.3f} seconds."
    )

    assert escape_maze(example, part_two=True) == 10

    start = time.time()
    steps = escape_maze(jump_offsets, part_two=True)
    duration = time.time() - start
    print(
        f"Part 2: exit reached in {steps:,} steps after {duration:.3f} seconds."
    )


if __name__ == "__main__":
    main()
