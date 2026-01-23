pub fn start_day(day: &str) {
    println!("Advent of Code 2025 - Day {:0>2}", day);
}

// Additional common functions

pub fn timed_result<T>(label: &str, f: impl FnOnce() -> anyhow::Result<T>) -> anyhow::Result<T> {
    let start = std::time::Instant::now();
    let out = f()?;
    eprintln!("{label} took {:?}", start.elapsed());
    Ok(out)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        start_day("00");
    }
}
