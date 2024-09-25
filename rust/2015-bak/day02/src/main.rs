fn get_dimensions(present: &str) -> (u32, u32, u32) {
    let dimensions: Vec<u32> = present
        .split('x')
        .map(|y| y.parse::<u32>().unwrap())
        .collect();

    let l = dimensions[0];
    let w = dimensions[1];
    let h = dimensions[2];

    (l, w, h)
}

fn process_part_one(input: &str) -> u32 {
    let mut total_paper = 0;
    for present in input.split('\n') {
        let (l, w, h) = get_dimensions(present);

        let lw = l * w;
        let wh = w * h;
        let hl = h * l;

        let slack = lw.min(wh).min(hl);

        let surface_area = 2 * lw + 2 * wh + 2 * hl;
        total_paper += surface_area + slack;
    }
    total_paper
}

fn process_part_two(input: &str) -> u32 {
    let mut total_ribbon = 0;
    for present in input.split('\n') {
        let (l, w, h) = get_dimensions(present);
        let mut dimensions = vec![l, w, h];
        dimensions.sort();
        let ribbon = 2 * dimensions[0] + 2 * dimensions[1];
        let bow = l * w * h;
        total_ribbon += ribbon + bow;
    }
    total_ribbon
}

fn main() {
    let input = include_str!("../input.txt");
    let part_one = process_part_one(input);
    println!("Part 1: {}", part_one);
    let part_two = process_part_two(input);
    println!("Part 2: {}", part_two);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(process_part_one("2x3x4"), 58);
        assert_eq!(process_part_one("1x1x10"), 43);
        assert_eq!(process_part_one("2x3x4\n1x1x10"), 101)
    }

    #[test]
    fn test_part2() {
        assert_eq!(process_part_two("2x3x4"), 34);
        assert_eq!(process_part_two("1x1x10"), 14);
        assert_eq!(process_part_two("2x3x4\n1x1x10"), 48)
    }
}
