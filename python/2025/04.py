import time
from aoc_helper import read_input_to_string, start_day

DAY = 4
EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


class Grid:
    def __init__(self, data: str) -> None:
        self.rows: list[list[int]] = [
            [int(c == "@") for c in row] for row in data.splitlines()
        ]
        self.width = len(self.rows[0])
        assert all(self.width == len(row) for row in self.rows)
        self.height = len(self.rows)

    def get(self, x: int, y: int) -> int:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.rows[y][x]
        return 0

    def get_neighbours(self, x: int, y: int) -> tuple[int, ...]:
        return tuple(
            self.get(x + dx, y + dy)
            for dy in (-1, 0, 1)
            for dx in (-1, 0, 1)
            if not (dx == 0 and dy == 0)
        )

    def __str__(self) -> str:
        return "\n".join("".join("@" if c else "." for c in row) for row in self.rows)


def part1(inputdata: str) -> int:
    grid = Grid(inputdata)
    result = 0
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) == 0:
                continue
            count = sum(grid.get_neighbours(x, y))
            result += int(count < 4)
    return result


def part2(inputdata: str) -> int:
    return len(inputdata.splitlines())


def main():
    start_day(DAY)

    assert part1(EXAMPLE) == 13
    inputdata = read_input_to_string(DAY)
    start = time.time()
    result = part1(inputdata)
    elapsed = time.time() - start
    print(f"Part 1: {result}, took {elapsed:.3f}s")

    assert part2(EXAMPLE) == 27
    start = time.time()
    result = part2(inputdata)
    elapsed = time.time() - start
    print(f"Part 2: {result}, took {elapsed:.3f}s")


if __name__ == "__main__":
    main()
