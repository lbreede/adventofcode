use adv_code_2019::*;
use anyhow::Result;
use anyhow::anyhow;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::Instant;

const DAY: &str = "01";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        reader
            .lines()
            .map(|line| {
                let line = line?;
                let mass = line.parse::<usize>()?;
                calc_fuel(mass)
            })
            .sum::<Result<usize>>()
    }

    assert_eq!(2, part1(BufReader::new("12".as_bytes()))?);
    assert_eq!(2, part1(BufReader::new("14".as_bytes()))?);
    assert_eq!(654, part1(BufReader::new("1969".as_bytes()))?);
    assert_eq!(33_583, part1(BufReader::new("100756".as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let start = Instant::now();
    let result = part1(input_file)?;
    let duration = start.elapsed();
    println!("{result} ({duration:?})");
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        reader
            .lines()
            .map(|line| {
                let line = line?;
                let mass = line.parse::<usize>()?;
                Ok(total_fuel(mass))
            })
            .sum::<Result<usize>>()
    }

    assert_eq!(2, part2(BufReader::new("14".as_bytes()))?);
    assert_eq!(966, part2(BufReader::new("1969".as_bytes()))?);
    assert_eq!(50346, part2(BufReader::new("100756".as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let start = Instant::now();
    let result = part2(input_file)?;
    let duration = start.elapsed();
    println!("{result} ({duration:?})");
    //endregion

    Ok(())
}

fn calc_fuel(mass: usize) -> Result<usize> {
    let fuel = mass / 3;
    fuel.checked_sub(2)
        .ok_or_else(|| anyhow!("overflow or underflow on input {}", fuel))
}

fn total_fuel(mass: usize) -> usize {
    match calc_fuel(mass) {
        Ok(fuel) => fuel + total_fuel(fuel),
        Err(_) => 0,
    }
}
