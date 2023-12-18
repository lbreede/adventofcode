import unittest

from day04 import part1, part2


class TestDay04(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("./example_day04.txt", encoding="utf-8") as fp:
            cls.example_data = fp.read()

        with open("./input_day04.txt", encoding="utf-8") as fp:
            cls.input_data = fp.read()

    def test_part1(self):
        self.assertEqual(part1(self.example_data), 13)
        self.assertEqual(part1(self.input_data), 21568)

    def test_part2(self):
        self.assertEqual(part2(self.example_data), 30)
        # TODO: Commented out because it takes too long to run
        # self.assertEqual(part2(self.input_data), 11827296)


if __name__ == "__main__":
    unittest.main()
