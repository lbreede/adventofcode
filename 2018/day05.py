# --- Day 5: Alchemical Reduction ---

import re
import os
from tqdm import trange


def create_regex():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    regex = ""
    for char in alphabet:
        regex += f"{char}{char.upper()}|{char.upper()}{char}|"
    return regex[:-1]


def reduce_(s, max_depth, depth=0):
    regex = create_regex()
    result = re.search(regex, s)
    if result and depth < max_depth:
        start, end = result.span()
        return reduce_(s[:start] + s[end:], max_depth, depth + 1)
    return s


def main():
    with open("day05_input.txt") as fp:
        string = fp.read()
    string = "dabAcCaCBAcCcaDA"

    for i in trange(30):
        string = reduce_(string, max_depth=900)

        regex = create_regex()
        if not re.search(regex, string):
            break

    print(string, "->", len(string))


if __name__ == "__main__":
    main()
