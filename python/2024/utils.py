from typing import IO, Callable, TypeVar
import io
import time


def assert_eq(a, b):
    assert a == b, f"{a} != {b}"


T = TypeVar("T")


def run(
    input_file: str, example: str, file_name: str, part: Callable[[IO], T], expected: T
) -> None:
    assert_eq(part(io.StringIO(example)), expected)

    with open(input_file, "r") as input_file:
        start = time.time()
        result = part(input_file)
        elapsed = time.time() - start
        print(f"{file_name} took {format_time(elapsed)}\nResult = {result}")


def format_time(seconds: float) -> str:
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.3f}μs"
    if seconds < 1.0:
        return f"{seconds * 1_000:.3f}ms"
    return f"{seconds:.3f}s"
    # TODO: add support for hours, minutes, etc.


def test_format_time() -> None:
    assert format_time(1.0) == "1.000s"
    assert format_time(0.999999) == "999.999ms"
    assert format_time(0.1) == "100.000ms"
    assert format_time(0.01) == "10.000ms"
    assert format_time(0.001) == "1.000ms"
    assert format_time(0.000999999) == "999.999μs"
    assert format_time(0.0001) == "100.000μs"
    assert format_time(0.00001) == "10.000μs"
    assert format_time(0.000001) == "1.000μs"
