from dataclasses import dataclass

from enum import Enum
import time
from typing import Self


class CardType(Enum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2


card_mapping = {
    "A": CardType.ACE,
    "K": CardType.KING,
    "Q": CardType.QUEEN,
    "J": CardType.JACK,
    "T": CardType.TEN,
    "9": CardType.NINE,
    "8": CardType.EIGHT,
    "7": CardType.SEVEN,
    "6": CardType.SIX,
    "5": CardType.FIVE,
    "4": CardType.FOUR,
    "3": CardType.THREE,
    "2": CardType.TWO,
}


class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __lt__(self, other: Self) -> bool:
        return self.value < other.value


@dataclass
class Hand:
    cards: list[CardType]
    bid: int

    @property
    def hand_type(self) -> HandType:
        counts = []
        for card_type in CardType:
            if c := self.cards.count(card_type):
                counts.append(c)
        counts.sort(reverse=True)

        if counts[0] == 5:
            return HandType.FIVE_OF_A_KIND
        if counts[0] == 4:
            return HandType.FOUR_OF_A_KIND
        if counts[0] == 3 and counts[1] == 2:
            return HandType.FULL_HOUSE
        if counts[0] == 3:
            return HandType.THREE_OF_A_KIND
        if counts[0] == 2 and counts[1] == 2:
            return HandType.TWO_PAIR
        if counts[0] == 2:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    @property
    def hand_score(self) -> int:
        score = 0
        for card in self.cards:
            score *= 100
            score += card.value
        return score

    def __lt__(self, other: Self) -> bool:
        if self.hand_type == other.hand_type:
            return self.hand_score < other.hand_score
        return self.hand_type < other.hand_type

    def __str__(self) -> str:
        cards = ", ".join(c.name for c in self.cards)
        return f"{self.hand_type.name:<16} | {cards:<32} | ${self.bid}"


def new_card(ch: str) -> CardType:
    if ch not in card_mapping:
        raise ValueError(f"Unknown character '{ch}'")
    return card_mapping[ch]


def part_one(file: str) -> int:
    hands = []
    with open(file, "r", encoding="utf-8") as fp:
        for line in fp:
            characters, bid = line.rstrip().split()
            cards = [new_card(ch) for ch in characters]
            bid = int(bid)
            hands.append(Hand(cards, bid))

    hands.sort()
    return sum((i + 1) * hand.bid for i, hand in enumerate(hands))


def part_two(file: str) -> int:
    return 0


def test_part_one():
    assert part_one("example_day07.txt") == 6_440
    assert part_one("input_day07.txt") == 248_422_077


def test_part_two():
    assert part_two("example_day07.txt") == 5_905


def run():
    print("Day 7: Camel Cards")
    start = time.time()
    result = part_one("input_day07.txt")
    elapsed = time.time() - start
    print(f"Part 1: {result:,} ({elapsed:.3f}s)")


if __name__ == "__main__":
    run()
