use std::collections::{HashMap, HashSet};

use scan_fmt::scan_fmt;

fn main () {
    let visited = solve(); 
    println!("{}\n{}", visited[1].len(), visited[9].len());
}

fn solve() -> Vec<HashSet<(i32, i32)>> {
    let input = include_str!("../input");
    let directions = HashMap::from([('U', (0, 1)), ('D', (0, -1)), ('L', (-1, 0)), ('R', (1, 0))]);

    let mut rope = [(0, 0); 10];
    let mut visited: Vec<HashSet<(i32, i32)>> = (0..10).map(|_| HashSet::new()).collect::<Vec<_>>();

    for line in input.lines() {
        let (d, n) = scan_fmt!(line, "{} {}", char, u16).unwrap();
        let (dx, dy) = directions.get(&d).unwrap();

        for _ in 0..n {
            rope[0] = (rope[0].0 + dx, rope[0].1 + dy);

            for idx in 1..rope.len() {
                let dx: i32 = rope[idx - 1].0 - rope[idx].0;
                let dy: i32 = rope[idx - 1].1 - rope[idx].1;
                if std::cmp::max(dx.abs(), dy.abs()) > 1 {
                    rope[idx] = (rope[idx].0 + dx.signum(), rope[idx].1 + dy.signum());
                }

                visited[idx].insert(rope[idx]);
            }
        }
    }

    return visited;        
}