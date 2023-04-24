use anyhow::{anyhow, Context, Result};
use std::str::FromStr;

fn main() -> Result<()> {
    let instructions = include_str!("../input")
        .lines()
        .map(Instruction::from_str)
        .collect::<Result<Vec<_>>>()?;

    let mut x_states: Vec<isize> = vec![0, 1];

    for instruction in instructions {
        let x_val = *x_states.last().context("unable to peek stack")?;
        match instruction {
            Instruction::Noop => {
                x_states.push(x_val);
            }
            Instruction::Addx(value) => {
                x_states.push(x_val);
                x_states.push(x_val + value);
            }
        }
    }

    let p1_cycles = (20..=220).step_by(40).collect::<Vec<_>>();
    let p1_answer = x_states
        .iter()
        .enumerate()
        .filter(|(cycle, _)| p1_cycles.contains(cycle))
        .map(|(cycle, x_val)| *x_val * (cycle as isize))
        .sum::<isize>();

    println!("Part 1 answer: {}", p1_answer);

    let mut out = String::new();

    for row in 0..6 {
        for col in 0..40 {
            let cycle = ((row * 40) + col) + 1;
            let x_val = x_states[cycle];
            let col = col as isize;

            if col == (x_val - 1) || col == x_val || col == (x_val + 1) {
                out.push('#');
            } else {
                out.push('.');
            }
        }

        out.push('\n');
    }

    println!("Part 2 answer:\n{}", out);

    Ok(())
}

#[derive(Debug, PartialEq)]
enum Instruction {
    Noop,
    Addx(isize),
}

impl FromStr for Instruction {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if s.starts_with("noop") {
            Ok(Instruction::Noop)
        } else if s.starts_with("addx") {
            let p = s[5..]
                .parse::<isize>()
                .context("unable to parse addx parameter")?;
            Ok(Instruction::Addx(p))
        } else {
            Err(anyhow!(format!("invalid instruction {}", s)))
        }
    }
}
