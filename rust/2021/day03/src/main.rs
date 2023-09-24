fn part_one(input: String) -> u32 {
    let length = input.lines().nth(0).unwrap().len();

    let mut bgamma= String::new();
    let mut bepsilon = String::new();

    for i in 0..length {
        let mut bits = Vec::new();
        for line in input.lines() {
            bits.push(line.chars().nth(i).unwrap());
        }
        let count_ones = bits.iter().filter(|&x| *x == '1').count();
        let count_zeros = bits.iter().filter(|&x| *x == '0').count();

        if count_ones > count_zeros {
            bgamma.push('1');
            bepsilon.push('0');
        } else {
            bgamma.push('0');
            bepsilon.push('1');
        }
    }
    let gamma = u32::from_str_radix(&bgamma, 2).unwrap();
    let epsilon = u32::from_str_radix(&bepsilon, 2).unwrap();
    gamma * epsilon
}

fn part_two(input: String) -> u32 {
    let length = input.lines().nth(0).unwrap().len();
    let lines = input.lines().into_iter().collect::<Vec<&str>>();

    for i in 0..length {
        lines = lines.filter(|&line| {
            let mut bits = Vec::new();
            for line in input.lines() {
                bits.push(line.chars().nth(i).unwrap());
            }
            let count_ones = bits.iter().filter(|&x| *x == '1').count();
            let count_zeros = bits.iter().filter(|&x| *x == '0').count();

            if count_ones > count_zeros {
                return line.chars().nth(i).unwrap() == '1';
            } else {
                return line.chars().nth(i).unwrap() == '0';
            }
        })
    }

    // for i in 0..length {
    //     let mut bits = Vec::new();
    //     for line in &lines {
    //         bits.push(line.chars().nth(i).unwrap());
    //     }
    //     let count_ones = bits.iter().filter(|&x| *x == '1').count();
    //     let count_zeros = bits.iter().filter(|&x| *x == '0').count();

    //     let mut lines2: Vec<&str> = Vec::new();
    //     if count_ones >= count_zeros {
    //         for line in &lines {
    //             if line.chars().nth(i).unwrap() == '1' {
    //                 lines2.push(line);
    //             }
    //         }
    //     } else {
    //         for line in &lines {
    //             if line.chars().nth(i).unwrap() == '0' {
    //                 lines2.push(line);
    //             }
    //         }
    //     }
    //     // println!("{:?}", lines2);
    //     let lines = lines2;

    //     // println!("{} {}", count_ones, count_zeros);
    // }
    0
}

fn main() {
    let input = include_str!("../input.txt");
    println!("Part One: {}", part_one(input.to_string()));
    println!("Part Two: {}", part_two(input.to_string()));
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE: &str = include_str!("../example.txt");
    const INPUT: &str = include_str!("../input.txt");

    #[test]
    fn test_part_one() {
        assert_eq!(part_one(EXAMPLE.to_string()), 198);
        assert_eq!(part_one(INPUT.to_string()), 4147524);
    }

    #[test]
    fn test_part_two() {
        assert_eq!(part_two(EXAMPLE.to_string()), 230);
        // assert_eq!(part_two(INPUT.to_string()), 0);
    }
}
