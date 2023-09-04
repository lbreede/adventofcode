fn parse_input(input: String) -> Vec<u32> {
    input.lines().map(|line| line.parse().unwrap()).collect()
}

fn count_increased(parsed: Vec<u32>) -> u32 {
    let mut parsed = parsed.into_iter().peekable();
    let mut count = 0;
    while let Some(a) = parsed.next() {
        if let Some(b) = parsed.peek() {
            if a < *b {
                count += 1;
            }
        }
    }
    count
}

fn part_one(input: String) -> u32 {
    let lines = parse_input(input);
    count_increased(lines)
}

fn part_two(input: String) -> u32 {
    let lines = parse_input(input);
    let windows = lines.windows(3).map(|window| window.iter().sum()).collect();
    count_increased(windows)
}

fn main() {
    let input = include_str!("../input.txt");
    println!("Part one: {}", part_one(input.to_string()));
    println!("Part two: {}", part_two(input.to_string()));
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = include_str!("../example.txt");
    const INPUT: &str = include_str!("../input.txt");

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(EXAMPLE.to_string()), 7);
        assert_eq!(part_one(INPUT.to_string()), 1167);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(EXAMPLE.to_string()), 5);
        assert_eq!(part_two(INPUT.to_string()), 1130);
    }
}
