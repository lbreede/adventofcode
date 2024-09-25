use std::collections::HashMap;

#[derive(Debug)]
struct Monkey {
    items: Vec<u32>,
    operation: String,
    test_value: u32,
    if_true: u32,
    if_false: u32,
}

fn part_one(input: String) -> u32 {
    let monkeys = get_monkeys(input);
    println!("{:?}\n\n", monkeys);
    0
}

fn get_monkeys(input: String) -> HashMap<u32, Monkey> {
    let mut monkeys: HashMap<u32, Monkey> = HashMap::new();

    for m in input.split("\n\n") {
        let lines = m.split("\n").collect::<Vec<&str>>();

        let number = lines[0].split_whitespace().collect::<Vec<&str>>()[1]
            .chars()
            .collect::<Vec<char>>()[0]
            .to_digit(10)
            .unwrap();

        let items = lines[1].split(": ").collect::<Vec<&str>>()[1]
            .split(", ")
            .collect::<Vec<&str>>()
            .iter()
            .map(|s| s.parse::<u32>().unwrap())
            .collect::<Vec<u32>>();

        let operation = lines[2].split(": ").collect::<Vec<&str>>()[1];

        let test_value = lines[3].split_whitespace().collect::<Vec<&str>>()[3]
            .parse::<u32>()
            .unwrap();

        let if_true = lines[4].split_whitespace().collect::<Vec<&str>>()[5]
            .parse::<u32>()
            .unwrap();
        let if_false = lines[5].split_whitespace().collect::<Vec<&str>>()[5]
            .parse::<u32>()
            .unwrap();

        monkeys.insert(
            number,
            Monkey {
                items: items,
                operation: operation.to_string(),
                test_value: test_value,
                if_true: if_true,
                if_false: if_false,
            },
        );
    }
    monkeys
}

fn main() {
    let input = include_str!("../input.txt");
    println!("Part one: {}", part_one(input.to_string()));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = include_str!("../example.txt");
        assert_eq!(part_one(input.to_string()), 10605);
    }
}
