# --- Day 4: Giant Squid ---

from pprint import pprint
from typing import Optional


class BingoBoard:
    def __init__(self, data: str, ident: Optional[int] = None) -> None:
        self.numbers = self._get_board(data)
        self._truth = [[False for _ in range(5)] for _ in range(5)]
        self.ident = ident
        self._last_guessed = None
        self.score = 0

    @staticmethod
    def _get_board(data: str) -> list[list[int]]:
        return [[int(num) for num in row.split()] for row in data.splitlines()]

    def check_number(self, number: int) -> None:
        for i, row in enumerate(self.numbers):
            if number in row:
                print(f"Found {number} in row {i+1}")
                self._truth[i][row.index(number)] = True
        self._last_guessed = number

    def check_rows(self) -> bool:
        for row in self._truth:
            if all(row):
                return True
        return False

    def check_columns(self) -> bool:
        for i in range(5):
            if all([row[i] for row in self._truth]):
                return True
        return False

    # def check_diagonals(self) -> bool:
    #     if all([self._truth[i][i] for i in range(5)]):
    #         return True
    #     if all([self._truth[i][4-i] for i in range(5)]):
    #         return True
    #     return False

    def _check_bingo(self) -> bool:
        return (
            self.check_rows() or self.check_columns()
        )  # or self.check_diagonals()

    def get_score(self) -> int:
        if self._check_bingo():
            score = 0
            pprint(self.numbers)
            pprint(self._truth)
            for i, row in enumerate(self.numbers):
                for j, num in enumerate(row):
                    if not self._truth[i][j]:
                        print(num)
                        score += num
            return score * self._last_guessed
        return 0


def get_numbers(data: str) -> list[int]:
    return [int(num) for num in data.split("\n\n")[0].split(",")]


def get_bingo_boards(data: str) -> list[BingoBoard]:
    return [
        BingoBoard(board, i + 1)
        for i, board in enumerate(data.split("\n\n")[1:])
    ]


def main() -> None:
    with open("day04_input.txt", encoding="utf-8") as fp:
        data = fp.read()

    numbers = get_numbers(data)
    boards = get_bingo_boards(data)

    for number in numbers:
        for board in boards:
            board.check_number(number)
            score = board.get_score()
            if score:
                print(f"Board {board.ident} has bingo with score {score}")
                break
        else:
            continue
        break


if __name__ == "__main__":
    main()
