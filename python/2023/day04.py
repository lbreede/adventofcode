def part1(data: str) -> int:
    result = 0
    for game in data.splitlines():
        a, b = game.split(": ")[1].split(" | ")
        a = set(int(x) for x in a.split())
        b = set(int(x) for x in b.split())
        intersection = len(a.intersection(b))
        if intersection:
            result += 2 ** (intersection - 1)
    return result


def part2(data: str) -> int:
    game_dict: dict[int, int] = {}
    for game in data.splitlines():
        num, scores = game.split(": ")
        num = int(num.split()[1])
        a, b = scores.split(" | ")
        a = set(int(x) for x in a.split())
        b = set(int(x) for x in b.split())
        intersection = len(a.intersection(b))
        game_dict[num] = intersection

    repeat_dict = {k: 1 for k in game_dict}

    result = 0
    for k, v in game_dict.items():
        for _ in range(repeat_dict[k]):
            result += 1
            for i in range(1, v + 1):
                repeat_dict[k + i] += 1
    return result


def main() -> None:
    with open("./input_day04.txt", encoding="utf-8") as fp:
        data = fp.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
