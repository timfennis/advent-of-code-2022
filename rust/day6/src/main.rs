use std::collections::HashSet;

use itertools::Itertools;

fn main() {
    let input = include_str!("../input");
    println!("{}", find_start_sequence(input, 4));
    println!("{}", find_start_sequence(input, 14));
}

fn find_start_sequence(sequqnce: &str, len: usize) -> usize {
    return sequqnce
        .as_bytes()
        .windows(len)
        .find_position(|w| w.iter().collect::<HashSet<_>>().len() == len)
        .unwrap()
        .0
}