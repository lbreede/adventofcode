from typing import Optional


def get_neighbour(
    lines: list[str], row: int, start_col: int, end_col: int
) -> Optional[str]:
    height = len(lines)
    width = len(lines[0])

    if row - 1 >= 0:
        for col in range(max(start_col - 1, 0), min(end_col + 1, width - 1)):
            symbol = lines[row - 1][col]
            if symbol != ".":
                return symbol

    if row + 1 < height:
        for col in range(max(start_col - 1, 0), min(end_col + 1, width - 1)):
            symbol = lines[row + 1][col]
            if symbol != ".":
                return symbol

    if start_col - 1 >= 0:
        symbol = lines[row][start_col - 1]
        if symbol != ".":
            return symbol

    if end_col < width:
        symbol = lines[row][end_col]
        if symbol != ".":
            return symbol


def part1(data: str) -> int:
    result = 0
    lines = data.splitlines()
    start_col: Optional[int] = None
    number = ""
    for row, line in enumerate(lines):
        line += "."
        for col, char in enumerate(line):
            # Check if current character is a digit or not
            if char.isdigit():
                # If there's currently no number, we start a new one and save its column
                if not number:
                    start_col = col
                number += char
            else:
                # Check if there's a number before the current character
                if number.isdigit():
                    assert isinstance(start_col, int)
                    neighbour = get_neighbour(lines, row, start_col, col)
                    if neighbour is not None:
                        result += int(number)
                    number = ""
    return result


def get_gear_coord(
    lines: list[str], row: int, start_col: int, end_col: int
) -> Optional[str]:
    height = len(lines)
    width = len(lines[0])

    if row - 1 >= 0:
        for col in range(max(start_col - 1, 0), min(end_col + 1, width - 1)):
            symbol = lines[row - 1][col]
            if symbol == "*":
                return f"{row-1}x{col}"

    if row + 1 < height:
        for col in range(max(start_col - 1, 0), min(end_col + 1, width - 1)):
            symbol = lines[row + 1][col]
            if symbol == "*":
                return f"{row+1}x{col}"

    if start_col - 1 >= 0:
        symbol = lines[row][start_col - 1]
        if symbol == "*":
            return f"{row}x{start_col-1}"

    if end_col < width:
        symbol = lines[row][end_col]
        if symbol == "*":
            return f"{row}x{end_col}"


def part2(data: str) -> int:
    lines = data.splitlines()
    start_col: Optional[int] = None
    number = ""

    gear_dict: dict[str, list[int]] = {}

    for row, line in enumerate(lines):
        line += "."
        for col, char in enumerate(line):
            # Check if current character is a digit or not
            if char.isdigit():
                # If there's currently no number, we start a new one and save its column
                if not number:
                    start_col = col
                number += char
            else:
                # Check if there's a number before the current character
                if number.isdigit():
                    assert isinstance(start_col, int)
                    coord = get_gear_coord(lines, row, start_col, col)
                    if coord is not None:
                        if coord not in gear_dict:
                            gear_dict[coord] = [int(number)]
                        else:
                            gear_dict[coord].append(int(number))
                    number = ""

    result = 0
    for val in gear_dict.values():
        if len(val) == 2:
            result += val[0] * val[1]
    return result


def main() -> None:
    with open("./input_day03.txt", encoding="utf-8") as fp:
        data = fp.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
