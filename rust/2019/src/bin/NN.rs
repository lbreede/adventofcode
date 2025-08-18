use adv_code_2019::*;
use anyhow::Result;
use const_format::concatcp;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::Instant;

const DAY: &str = "NN"; // TODO: Fill the day
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "\
<TEST-INPUT>
"; // TODO: Add the test input

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        // TODO: Solve Part 1 of the puzzle
        let answer = reader.lines().map_while(Result::ok).count();
        Ok(answer)
    }

    // TODO: Set the expected answer for the test input
    assert_eq!(0, part1(BufReader::new(EXAMPLE.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let start = Instant::now();
    let result = part1(input_file)?;
    let duration = start.elapsed();
    println!("{result} ({duration:?})");
    //endregion

    //region Part 2
    // println!("\n=== Part 2 ===");
    //
    // fn part2<R: BufRead>(reader: R) -> Result<usize> {
    //     let answer = reader.lines().map_while(Result::ok).count();
    //     Ok(answer)
    // }
    //
    // assert_eq!(0, part2(BufReader::new(EXAMPLE.as_bytes()))?);
    //
    // let input_file = BufReader::new(File::open(INPUT_FILE)?);
    // let start = Instant::now();
    // let result = part2(input_file)?;
    // let duration = start.elapsed();
    // println!("{result} ({duration:?})");
    //endregion

    Ok(())
}
