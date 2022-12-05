use itertools::Itertools;
use scan_fmt::scan_fmt;

fn main() {
    solve(true);
    solve(false);
}

fn solve(part1: bool) {
    let input = include_str!("../input").split("\n\n").collect::<Vec<_>>();
    let config = *input.get(0).unwrap();
    let moves = *input.get(1).unwrap();

    let mut stacks: Vec<Vec<char>> = Vec::new();

    for line in config.lines().rev() {
        for (idx, char) in line.chars().enumerate() {
            if char.is_alphabetic() {
                let pos = (idx - 1) / 4;
                if let Some(stack) = stacks.get_mut(pos) {
                    stack.push(char);
                } else {
                    stacks.push(vec![char]);
                }
            }
        }
    }

    for line in moves.lines() {
        let (amount, from, to) =
            scan_fmt!(line, "move {d} from {d} to {d}", usize, usize, usize).unwrap();

        let from_len = stacks[from - 1].len();
        let mut slice = stacks[from - 1][from_len - amount..from_len].to_vec();

        if part1 {
            slice.reverse();
        }

        stacks[from - 1].truncate(from_len - amount);
        stacks[to - 1].append(&mut slice);
    }

    let top = stacks.iter().map(|stack| stack.last().unwrap()).join("");

    println!("{}", top);
}
