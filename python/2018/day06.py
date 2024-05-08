# --- Day 6: Chronal Coordinates ---

from pathlib import Path
from string import ascii_uppercase, ascii_lowercase
from os import PathLike
from typing import Optional

Coord = tuple[int, int]
CoordList = list[Coord]


def targets_from_file(file: PathLike) -> CoordList:
    targets: CoordList = []
    with open(file, "r", encoding="utf-8") as fp:
        for line in fp:
            x, y = (int(n) for n in line.strip().split(", "))
            targets.append((x, y))
    return targets


def manhatten_distance(a: Coord, b: Coord) -> int:
    return abs(b[0] - a[0]) + abs((b[1] - a[1]))


def find_target(coord: Coord, targets: CoordList) -> Optional[int]:
    dists = [manhatten_distance(coord, target) for target in targets]
    min_dist = min(dists)

    if dists.count(min_dist) != 1:
        return

    index = dists.index(min_dist)
    if min_dist == 0:
        return index
    return index


def print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print("".join(row))


def main():
    file = Path("day06_input.txt")
    targets = targets_from_file(file)

    x_min = min(x for x, _ in targets)
    x_max = max(x for x, _ in targets)
    y_min = min(y for _, y in targets)
    y_max = max(y for _, y in targets)

    scores_wide: dict[int, int] = {}
    scores_narrow: dict[int, int] = {}
    for j in range(y_min, y_max + 1):
        for i in range(x_min, x_max + 1):
            target = find_target((i, j), targets)
            if target is None:
                continue

            if target not in scores_wide:
                scores_wide[target] = 1
            else:
                scores_wide[target] += 1

            if i != x_min and i != x_max and j != y_min and j != y_max:
                if target not in scores_narrow:
                    scores_narrow[target] = 1
                else:
                    scores_narrow[target] += 1

    largest_area = 0
    for k, v in scores_narrow.items():
        if scores_narrow[k] == scores_wide[k]:
            largest_area = max(largest_area, v)
    print(f"Part 1: The largest area that isn't infinite is {largest_area}")


if __name__ == "__main__":
    main()
