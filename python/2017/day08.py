# --- Day 8: I Heard You Like Registers ---


def passed(lhs: int, cond: str, rhs: int) -> bool:
    if cond == ">":
        return lhs > rhs
    if cond == "<":
        return lhs < rhs
    if cond == ">=":
        return lhs >= rhs
    if cond == "<=":
        return lhs <= rhs
    if cond == "==":
        return lhs == rhs
    if cond == "!=":
        return lhs != rhs
    return False


def modify_registers(filename: str) -> tuple[int, int]:
    registers: dict[str, int] = {}
    current_highest = all_time_highest = 0
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            name, operation, value, _, lhs, cond, rhs = line.split()

            if passed(registers.get(lhs, 0), cond, int(rhs)):
                continue
            
            val = int(value) if operation == "inc" else -int(value)
            registers[name] = registers.get(name, 0) + val

            current_highest = max(registers.values())
            if current_highest > all_time_highest:
                all_time_highest = current_highest

    return current_highest, all_time_highest


def main() -> None:
    assert modify_registers("day08_example.txt") == (1, 10)

    solution_one, solution_two = modify_registers("day08_input.txt")
    print(f"Part one: {solution_one}")
    print(f"Part two: {solution_two}")


if __name__ == "__main__":
    main()
