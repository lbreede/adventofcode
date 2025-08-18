#[derive(Debug)]
pub struct IntcodeComputer {
    memory: Vec<i32>,
}

impl IntcodeComputer {
    pub fn new(memory: Vec<i32>) -> Self {
        Self { memory }
    }

    pub fn set_noun(&mut self, noun: i32) {
        self.memory[1] = noun
    }

    pub fn set_verb(&mut self, verb: i32) {
        self.memory[2] = verb
    }

    pub fn run(&mut self) {
        let mut ptr = 0;
        loop {
            match self.memory[ptr] {
                1 => {
                    let lhs = self.memory[self.memory[ptr + 1] as usize];
                    let rhs = self.memory[self.memory[ptr + 2] as usize];
                    let idx = self.memory[ptr + 3];
                    self.memory[idx as usize] = lhs + rhs;
                    ptr += 4;
                }
                2 => {
                    let lhs = self.memory[self.memory[ptr + 1] as usize];
                    let rhs = self.memory[self.memory[ptr + 2] as usize];
                    let idx = self.memory[ptr + 3];
                    self.memory[idx as usize] = lhs * rhs;
                    ptr += 4;
                }
                99 => break,
                op => unimplemented!("unknown opcode: {op}"),
            }
        }
    }

    pub fn first(&self) -> Option<&i32> {
        self.memory.first()
    }
}

impl From<&str> for IntcodeComputer {
    fn from(value: &str) -> Self {
        Self {
            memory: value
                .trim()
                .split(',')
                .map(|s| s.trim().parse::<i32>().unwrap())
                .collect(),
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::intcode::IntcodeComputer;
    use std::fs::File;
    use std::io::BufRead;
    use std::io::BufReader;

    mod day02 {

        use super::*;

        #[test]
        fn example01() {
            let mut computer = IntcodeComputer::from("1,9,10,3,2,3,11,0,99,30,40,50");
            computer.run();
            assert_eq!(
                computer.memory,
                vec![3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
            )
        }
        #[test]
        fn example02() {
            let mut computer = IntcodeComputer::from("1,0,0,0,99");
            computer.run();
            assert_eq!(computer.memory, vec![2, 0, 0, 0, 99])
        }
        #[test]
        fn example03() {
            let mut computer = IntcodeComputer::from("2,3,0,3,99");
            computer.run();
            assert_eq!(computer.memory, vec![2, 3, 0, 6, 99])
        }
        #[test]
        fn example04() {
            let mut computer = IntcodeComputer::from("2,4,4,5,99,0");
            computer.run();
            assert_eq!(computer.memory, vec![2, 4, 4, 5, 99, 9801])
        }
        #[test]
        fn example05() {
            let mut computer = IntcodeComputer::from("1,1,1,4,99,5,6,0,99");
            computer.run();
            assert_eq!(computer.memory, vec![30, 1, 1, 4, 2, 5, 6, 0, 99])
        }
        #[test]
        fn part1() {
            let reader = BufReader::new(File::open("input/02.txt").unwrap());
            let line = reader.lines().next().unwrap().unwrap();
            let mut computer = IntcodeComputer::from(line.as_str());
            computer.set_noun(12);
            computer.set_verb(2);
            computer.run();
            assert_eq!(computer.first(), Some(&3058646))
        }
        #[test]
        fn part2() {
            let reader = BufReader::new(File::open("input/02.txt").unwrap());
            let line = reader.lines().next().unwrap().unwrap();
            let mut computer = IntcodeComputer::from(line.as_str());
            computer.set_noun(89);
            computer.set_verb(76);
            computer.run();
            assert_eq!(computer.first(), Some(&19690720))
        }
    }
}
