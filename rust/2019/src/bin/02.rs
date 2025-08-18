use adv_code_2019::*;
use anyhow::{Result, anyhow};
use const_format::concatcp;
use intcode::IntcodeComputer;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::Instant;

const DAY: &str = "02";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<i32> {
        let line = reader
            .lines()
            .next()
            .ok_or_else(|| anyhow!("empty input"))??;
        let mut computer = IntcodeComputer::from(line.as_str());
        computer.set_noun(12);
        computer.set_verb(2);
        computer.run();
        computer
            .first()
            .copied()
            .ok_or_else(|| anyhow!("memory empty"))
    }
    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let start = Instant::now();
    let result = part1(input_file)?;
    let duration = start.elapsed();
    println!("{result} ({duration:?})");
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<i32> {
        let line = reader
            .lines()
            .next()
            .ok_or_else(|| anyhow!("empty input"))??;
        for noun in 0..=99 {
            for verb in 0..=99 {
                let mut computer = IntcodeComputer::from(line.as_str());
                computer.set_noun(noun);
                computer.set_verb(verb);
                computer.run();

                if let Some(&output) = computer.first() {
                    if output == 19_690_720 {
                        return Ok(100 * noun + verb);
                    }
                }
            }
        }
        anyhow::bail!("could not find noun-verb-combination that produces 19690720")
    }

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let start = Instant::now();
    let result = part2(input_file)?;
    let duration = start.elapsed();
    println!("{result} ({duration:?})");
    //endregion

    Ok(())
}
