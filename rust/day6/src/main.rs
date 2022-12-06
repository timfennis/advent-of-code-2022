use std::collections::HashSet;

fn main() {
    let input = include_str!("../input");
    println!("{}", find_start_sequence(input, 4));
    println!("{}", find_start_sequence(input, 14));
}

fn find_start_sequence(sequence: &str, size: usize) -> usize {
    for (idx, _) in sequence.chars().enumerate() {
        if idx >= size {
            let sub_seq: HashSet<char> = sequence[idx-size..idx].chars().collect::<_>();

            if sub_seq.len() == size {
                return idx
            }
        }
    }

    return 0
}