fn part_one(input: &str) -> u32 {
    let mut result = 0;
    for line in input.lines() {
        let digits = line
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect::<Vec<u32>>();
        result += 10 * digits.first().unwrap() + digits.last().unwrap();
    }
    result
}

fn part_two(input: &str) -> u32 {
    let mut result = 0;
    for line in input.lines() {
        let new_line = line
            .replace("one", "o1ne")
            .replace("two", "t2wo")
            .replace("three", "t3hree")
            .replace("four", "f4our")
            .replace("five", "f5ive")
            .replace("six", "s6ix")
            .replace("seven", "s7even")
            .replace("eight", "e8ight")
            .replace("nine", "n9ine");
        let digits = new_line
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect::<Vec<u32>>();
        result += 10 * digits.first().unwrap() + digits.last().unwrap();
    }
    result
}

fn main() {
    let input = include_str!("./input.txt");
    let result_one = part_one(input);
    println!("Part one: {}", result_one);
    let result_two = part_two(input);
    println!("Part two: {}", result_two);
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";

    const EXAMPLE_2: &str = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";

    #[test]
    fn part_one_works() {
        let result = part_one(EXAMPLE);
        assert_eq!(result, 142);
    }

    #[test]
    fn part_two_works() {
        let result = part_two(EXAMPLE_2);
        assert_eq!(result, 281);
    }
}
