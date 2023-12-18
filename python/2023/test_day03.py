import unittest

from day03 import part1, part2


class TestDay03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("./example_day03.txt", encoding="utf-8") as fp:
            cls.example_data = fp.read()

        with open("./input_day03.txt", encoding="utf-8") as fp:
            cls.input_data = fp.read()

    def test_part1(self):
        self.assertEqual(part1(self.example_data), 4361)
        self.assertEqual(part1(".....\n.123.\n....."), 0)
        self.assertEqual(part1("..*..\n.123.\n....."), 123)
        self.assertEqual(part1(".123\n..*."), 123)
        self.assertEqual(part1(self.input_data), 509115)

    def test_part2(self):
        self.assertEqual(part2(self.example_data), 467835)
        self.assertEqual(part2("...123...\n.456*789."), 0)
        self.assertEqual(part2(self.input_data), 75220503)


if __name__ == "__main__":
    unittest.main()
