use std::collections::{BinaryHeap, HashMap, HashSet};

fn get_dir(char: char) -> Option<(i32, i32)> {
    match char {
        '>' => Some((0, 1)),
        '<' => Some((0, -1)),
        'v' => Some((1, 0)),
        '^' => Some((-1, 0)),
        _ => None,
    }
}

type Blizzard = (i32, i32, i32, i32);

fn main() {
    let input = include_str!("../input");

    let blizz: Vec<Blizzard> = input
        .lines()
        .enumerate()
        .flat_map(|(row, line)| {
            line.chars().enumerate().filter_map(move |(col, char)| {
                get_dir(char).map(|dir| (row as i32 - 1, col as i32 - 1, dir.0, dir.1))
            })
        })
        .collect();

    let max_col = blizz.iter().map(|x| x.1).max().unwrap() as i32;
    let max_row = blizz.iter().map(|x| x.0).max().unwrap() as i32;
    let answer = solve((-1, 0), (25, 119), 0, &blizz, max_row, max_col);
    println!("Part 1: {answer}");

    let answer = solve((-1, 0), (25, 119), 2, &blizz, max_row, max_col);
    println!("Part 2: {answer}");
}

fn solve(
    start: (i32, i32),
    end: (i32, i32),
    repeats: u8,
    blizz: &Vec<Blizzard>,
    max_row: i32,
    max_col: i32,
) -> i32 {
    let mut blizz = blizz.to_owned();
    let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)];
    let mut time = 1;
    let mut queue = Vec::new();
    let mut target = end;
    let mut repeats = repeats;
    queue.push(start);

    loop {
        for (row, col, dr, dc) in blizz.iter_mut() {
            *row = (*row + *dr).rem_euclid(max_row + 1);
            *col = (*col + *dc).rem_euclid(max_col + 1);
        }
        let mut next_queue = HashSet::new();

        'bfs: while let Some((cr, cc)) = queue.pop() {
            // Update the blizzard
            // println!("Evaluating {cr} {cc}");
            for (dr, dc) in dirs {
                let (nr, nc) = ((cr + dr), (cc + dc));
                if (nr, nc) == target {
                    if repeats == 0 {
                        return time;
                    } else if repeats % 2 == 0 {
                        repeats -= 1;
                        target = start;
                        next_queue.clear();
                        queue.clear();
                        next_queue.insert(end);
                        break 'bfs;
                    } else {
                        repeats -= 1;
                        target = end;
                        next_queue.clear();
                        queue.clear();
                        next_queue.insert(start);
                        break 'bfs;
                    }
                }
                if (nr, nc) != start && (nr < 0 || nr > max_row || nc < 0 || nc > max_col) {
                    continue;
                }
                if blizz.iter().any(|(br, bc, _, _)| *br == nr && *bc == nc) {
                    continue;
                }
                next_queue.insert((nr, nc));
            }
        }
        queue = Vec::from_iter(next_queue.into_iter());
        time += 1;
    }
}


fn all_blizzards(max_row: u32, max_col: u32) {
    for (row, col, dr, dc) in blizz.iter_mut() {
        *row = (*row + *dr).rem_euclid(max_row + 1);
        *col = (*col + *dc).rem_euclid(max_col + 1);
    }
}
fn solve_prio(
    start: (i32, i32),
    end: (i32, i32),
    repeats: u8,
    blizz: &Vec<Blizzard>,
    max_row: i32,
    max_col: i32,
) -> i32 {
    let mut blizz = blizz.to_owned();
    let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)];
    let mut time = 1;
    let mut queue = Vec::new();
    let mut target = end;
    let mut repeats = repeats;
    queue.push(start);

    loop {
        'bfs: while let Some((cr, cc)) = queue.pop() {
            // Update the blizzard
            // println!("Evaluating {cr} {cc}");
            for (dr, dc) in dirs {
                let (nr, nc) = ((cr + dr), (cc + dc));
                if (nr, nc) == target {
                    if repeats == 0 {
                        return time;
                    } else if repeats % 2 == 0 {
                        repeats -= 1;
                        target = start;
                        next_queue.clear();
                        queue.clear();
                        next_queue.insert(end);
                        break 'bfs;
                    } else {
                        repeats -= 1;
                        target = end;
                        next_queue.clear();
                        queue.clear();
                        next_queue.insert(start);
                        break 'bfs;
                    }
                }
                if (nr, nc) != start && (nr < 0 || nr > max_row || nc < 0 || nc > max_col) {
                    continue;
                }
                if blizz.iter().any(|(br, bc, _, _)| *br == nr && *bc == nc) {
                    continue;
                }
                next_queue.insert((nr, nc));
            }
        }
        queue = Vec::from_iter(next_queue.into_iter());
        time += 1;
    }
}
