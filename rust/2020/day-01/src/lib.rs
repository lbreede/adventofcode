fn input_to_vec(input: &str) -> Vec<i32> {
    input
        .lines()
        .map(|line| line.parse::<i32>().unwrap())
        .collect::<Vec<i32>>()
}
pub fn process_part1(input: &str) -> String {
    let vec = input_to_vec(input);
    let n = vec.len();

    for i in 0..n {
        for j in (i + 1)..n {
            if vec[i] + vec[j] == 2020 {
                return (vec[i] * vec[j]).to_string();
            }
        }
    }
    "".to_string()
}

pub fn process_part2(input: &str) -> String {
    let vec = input_to_vec(input);
    let n = vec.len();
    for i in 0..n {
        for j in (i + 1)..n {
            for k in (j + 1)..n {
                if vec[i] + vec[j] + vec[k] == 2020 {
                    return (vec[i] * vec[j] * vec[k]).to_string();
                }
            }
        }
    }
    "".to_string()
}
#[cfg(test)]
mod tests {
    use super::*;
    const EXAMPLE: &str = "1721
979
366
299
675
1456";

    #[test]
    fn part1_works() {
        let result = process_part1(EXAMPLE);
        assert_eq!(result, "514579");
    }
    #[test]
    fn part2_works() {
        let result = process_part2(EXAMPLE);
        assert_eq!(result, "241861950");
    }
}
