# --- Day 6: Memory Reallocation ---

import time


def reallocate_memory(banks: list[int], part_two: bool = False) -> int:
    seen = [tuple(banks)]
    i = 1
    while True:
        val = max(banks)
        idx = banks.index(val)
        banks[idx] = 0
        for j in range(1, val + 1):
            banks[(idx + j) % len(banks)] += 1
        if tuple(banks) in seen:
            return len(seen) - seen.index(tuple(banks)) if part_two else i
        seen.append(tuple(banks))
        i += 1


def main() -> None:
    example = [0, 2, 7, 0]
    assert reallocate_memory(example.copy()) == 5

    with open("day06_input.txt", encoding="utf-8") as fp:
        banks = [int(x) for x in fp.read().split()]

    start = time.time()
    cycles = reallocate_memory(banks.copy())
    duration = time.time() - start
    print(f"Part 1: {cycles:,} cycles after {duration:.3f} seconds.")

    assert reallocate_memory(example, part_two=True) == 4

    start = time.time()
    cycles = reallocate_memory(banks, part_two=True)
    duration = time.time() - start
    print(f"Part 2: {cycles:,} cycles after {duration:.3f} seconds.")


if __name__ == "__main__":
    main()
