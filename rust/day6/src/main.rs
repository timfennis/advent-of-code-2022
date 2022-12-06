use std::collections::HashSet;

use itertools::Itertools;

fn main() {
    let input = include_str!("../input");
    println!("{}", find_start_sequence_alt(input, 4));
    println!("{}", find_start_sequence(input, 14));
}

/// Thieved from le reddit
fn find_start_sequence_alt(sequqnce: &str, len: usize) -> usize {
    return sequqnce
        .as_bytes()
        .windows(len)
        .enumerate()
        .find(|(_, w)| w.iter().collect::<HashSet<_>>().len() == len)
        .unwrap()
        .0 + len;
}

fn find_start_sequence(sequence: &str, size: usize) -> usize {
    for (idx, _) in sequence.chars().enumerate() {
        if idx >= size {
            let sub_seq: HashSet<char> = sequence[idx - size..idx].chars().collect::<_>();

            if sub_seq.len() == size {
                return idx;
            }
        }
    }

    return 0;
}
