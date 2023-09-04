use std::collections::HashSet;

#[derive(Debug, Hash, Eq, PartialEq)]
struct Location(i32, i32);

fn process_part_one(directions: String) -> u32 {
    let mut x = 0;
    let mut y = 0;
    let mut unique_set = HashSet::new();
    unique_set.insert(Location(x, y));
    for c in directions.chars() {
        match c {
            '^' => y += 1,
            '>' => x += 1,
            'v' => y -= 1,
            '<' => x -= 1,
            _ => {}
        }
        unique_set.insert(Location(x, y));
    }
    unique_set.len().try_into().unwrap()
}

fn process_part_two(directions: String) -> u32 {
    let mut x_santa = 0;
    let mut y_santa = 0;

    let mut x_robo = 0;
    let mut y_robo = 0;

    let mut unique_set = HashSet::new();
    unique_set.insert(Location(0, 0));

    for (i,c) in directions.chars().enumerate() {
        if i % 2 == 0 {
            match c {
                '^' => y_santa +=1,
                '>' => x_santa += 1,
                'v' => y_santa -= 1,
                '<' => x_santa -= 1,
                _ => {}
            }  
            unique_set.insert(Location(x_santa, y_santa));
        } else {
            match c {
                '^' => y_robo +=1,
                '>' => x_robo += 1,
                'v' => y_robo -= 1,
                '<' => x_robo -= 1,
                _ => {},
            }  
            unique_set.insert(Location(x_robo, y_robo));
        }
    }
    unique_set.len().try_into().unwrap()
}

fn main() {
    let input = include_str!("../input.txt");
    let part_one = process_part_one(input.to_string());
    println!("Part 1: {}", part_one);
    let part_two = process_part_two(input.to_string());
    println!("Part 2: {}", part_two);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(process_part_one(">".to_string()), 2);
        assert_eq!(process_part_one("^>v<".to_string()), 4);
        assert_eq!(process_part_one("^v^v^v^v^v".to_string()), 2);
    }

    #[test]
    fn test_part2() {
        assert_eq!(process_part_two("^v".to_string()), 3);
        assert_eq!(process_part_two("^>v<".to_string()), 3);
        assert_eq!(process_part_two("^v^v^v^v^v".to_string()), 11);
    }
}
