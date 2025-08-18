use adv_code_2019::start_day;
use anyhow::Result;
use anyhow::anyhow;
use const_format::concatcp;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::str::FromStr;
use std::time::Instant;

const DAY: &str = "03";
const INPUT_FILE: &str = concatcp!("input/", DAY, ".txt");

const EXAMPLE: &str = "R8,U5,L5,D3
U7,R6,D4,L4";
const EXAMPLE2: &str = "R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"; // = distance 159
const EXAMPLE3: &str = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"; // = distance

fn main() -> Result<()> {
    start_day(DAY);

    //region Part 1
    println!("=== Part 1 ===");

    fn part1<R: BufRead>(reader: R) -> Result<usize> {
        let (wire_a, wire_b) = parse_wires(reader)?;
        wire_a
            .visited
            .keys()
            .filter(|p| wire_b.visited.contains_key(p))
            .map(|p| p.manhattan())
            .min()
            .ok_or_else(|| anyhow!("no intersections found"))
    }

    assert_eq!(6, part1(BufReader::new(EXAMPLE.as_bytes()))?);
    assert_eq!(159, part1(BufReader::new(EXAMPLE2.as_bytes()))?);
    assert_eq!(135, part1(BufReader::new(EXAMPLE3.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let start = Instant::now();
    let result = part1(input_file)?;
    let duration = start.elapsed();
    println!("{result} ({duration:?})");
    //endregion

    //region Part 2
    println!("\n=== Part 2 ===");

    fn part2<R: BufRead>(reader: R) -> Result<usize> {
        let (wire_a, wire_b) = parse_wires(reader)?;
        wire_a
            .visited
            .keys()
            .filter(|p| wire_b.visited.contains_key(p))
            .map(|p| {
                let index_a = wire_a.visited.get(p).unwrap();
                let index_b = wire_b.visited.get(p).unwrap();
                index_a + index_b
            })
            .min()
            .ok_or_else(|| anyhow!("no intersections found"))
    }

    assert_eq!(30, part2(BufReader::new(EXAMPLE.as_bytes()))?);
    // assert_eq!(610, part2(BufReader::new(EXAMPLE2.as_bytes()))?);
    // assert_eq!(410, part2(BufReader::new(EXAMPLE3.as_bytes()))?);

    let input_file = BufReader::new(File::open(INPUT_FILE)?);
    let start = Instant::now();
    let result = part2(input_file)?;
    let duration = start.elapsed();
    println!("{result} ({duration:?})");
    //endregion

    Ok(())
}

#[derive(Debug)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

#[derive(Debug)]
struct Movement {
    direction: Direction,
    distance: i32,
}

impl FromStr for Movement {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self> {
        let (dir, dist) = s.split_at(1);
        let direction = match dir {
            "U" => Direction::Up,
            "D" => Direction::Down,
            "L" => Direction::Left,
            "R" => Direction::Right,
            _ => return Err(anyhow!("unknown direction: {}", dir)),
        };
        let distance = dist.parse::<i32>()?;
        Ok(Movement {
            direction,
            distance,
        })
    }
}

#[derive(Debug, Clone, Copy, Hash, PartialEq, Eq)]
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }

    fn manhattan(&self) -> usize {
        (self.x.unsigned_abs() + self.y.unsigned_abs()) as usize
    }
}

#[derive(Debug)]
struct Wire {
    position: Point,
    step: usize,
    visited: HashMap<Point, usize>,
}

impl Wire {
    fn new() -> Self {
        Self {
            position: Point::new(0, 0),
            step: 0,
            visited: HashMap::new(), // HashSet::from([Point::new(0, 0)]),
        }
    }

    fn apply_movement(&mut self, movement: &Movement) {
        for _ in 0..movement.distance {
            match movement.direction {
                Direction::Up => self.position.y += 1,
                Direction::Down => self.position.y -= 1,
                Direction::Left => self.position.x -= 1,
                Direction::Right => self.position.x += 1,
            }
            self.step += 1;
            self.visited.entry(self.position).or_insert(self.step);
        }
    }

    fn apply_movements(&mut self, movements: &[Movement]) {
        for m in movements {
            self.apply_movement(m);
        }
    }
}

fn parse_line(line: &str) -> Result<Vec<Movement>> {
    line.split(',').map(|s| s.parse()).collect()
}

fn parse_wires<R: BufRead>(reader: R) -> Result<(Wire, Wire)> {
    let mut lines = reader.lines();

    let mut wire_a = Wire::new();
    let mut wire_b = Wire::new();
    for (i, wire) in [&mut wire_a, &mut wire_b].into_iter().enumerate() {
        let line = lines
            .next()
            .ok_or_else(|| anyhow!("missing line {}", i + 1))??;
        let movements = parse_line(&line)?;
        wire.apply_movements(&movements);
    }
    Ok((wire_a, wire_b))
}
