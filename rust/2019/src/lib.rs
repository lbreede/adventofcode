pub mod intcode;

pub fn start_day(day: &str) {
    println!("Advent of Code 2019 - Day {day:0>2}");
}

// Additional common functions

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        start_day("00");
    }
}
