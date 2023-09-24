def part_one(passphrase: str) -> bool:
    words = passphrase.split()
    return len(words) == len(set(words))


def part_two(passphrase: str) -> bool:
    passphrase = " ".join(["".join(sorted(word)) for word in passphrase.split()])
    return part_one(passphrase)


def main() -> None:
    assert part_one("aa bb cc dd ee")
    assert not part_one("aa bb cc dd aa")
    assert part_one("aa bb cc dd aaa")

    with open("day04_input.txt", encoding="utf-8") as fp:
        passphrases = fp.read().splitlines()

    solution = sum([part_one(p) for p in passphrases])
    print("Part 1:", solution)

    assert part_two("abcde fghij")
    assert not part_two("abcde xyz ecdab")
    assert part_two("a ab abc abd abf abj")
    assert part_two("iiii oiii ooii oooi oooo")
    assert not part_two("oiii ioii iioi iiio")

    solution = sum([part_two(p) for p in passphrases])
    print("Part 2:", solution)


if __name__ == "__main__":
    main()
