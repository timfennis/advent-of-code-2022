use std::collections::{HashMap, LinkedList};

type Point = (usize, usize);

const EXAMPLE_INPUT: &str = include_str!("../example");
const INPUT: &str = include_str!("../input");

fn main() {
    println!("Part 1: {}", solve(INPUT, false).unwrap());
    println!("part 2: {}", solve(INPUT, true).unwrap());
}

fn solve(input: &str, part_two: bool) -> Option<u32> {
    let mut grid: Vec<Vec<char>> = Vec::new();
    let mut start: Option<Point> = None;
    let mut end: Option<Point> = None;

    for (y, line) in input.lines().enumerate() {
        grid.push(Vec::new());
        for (x, char) in line.chars().enumerate() {
            match char {
                'S' => {
                    start = Some((y, x));
                    grid[y].insert(x, 'a')
                }
                'E' => {
                    end = Some((y, x));
                    grid[y].insert(x, 'z')
                }
                c => grid[y].insert(x, c),
            }
        }
    }

    return match (start, end, part_two) {
        (Some((start_y, start_x)), Some(end), false) => {
            find_shortest_path(&grid, start_x, start_y, false)
                .get(&end)
                .map(|&x| x)
        }
        (_, Some((end_y, end_x)), true) => find_shortest_path(&grid, end_x, end_y, true)
            .iter()
            .filter(|((y, x), _)| grid[*y][*x] == 'a' )
            .min_by(|(_, &v1), (_, &v2)| v1.cmp(&v2))
            .map(|(_, &v)| v),

        _ => None,
    };
}

fn find_shortest_path(
    grid: &Vec<Vec<char>>,
    start_x: usize,
    start_y: usize,
    reverse: bool,
) -> HashMap<Point, u32> {
    let directions: [(i16, i16); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];
    let mut paths: HashMap<Point, u32> = HashMap::new();
    let mut search_buffer: LinkedList<(usize, usize, u32)> = LinkedList::new();
    search_buffer.push_back((start_y, start_x, 0));

    while let Some((y, x, current_steps)) = search_buffer.pop_front() {
        'dir: for (dy, dx) in directions {
            let new_x: i16 = x as i16 + dx;
            let new_y: i16 = y as i16 + dy;

            // Check if this delta is out of bounds or not
            if new_x < 0 || new_x >= grid[0].len() as i16 || new_y < 0 || new_y >= grid.len() as i16
            {
                continue;
            }

            let new_x = new_x as usize;
            let new_y = new_y as usize;

            let from_height = grid[y][x] as i8;
            let to_height = grid[new_y][new_x] as i8;

            match (reverse, to_height - from_height) {
                (false, n) => {
                    if n > 1 {
                        continue 'dir;
                    }
                }
                (true, n) => {
                    if n < -1 {
                        continue 'dir;
                    }
                }
            }

            match paths.get(&(new_y, new_x)) {
                Some(&current_best) => {
                    if current_steps + 1 < current_best {
                        paths.insert((new_y, new_x), current_steps + 1);
                        search_buffer.push_back((new_y, new_x, current_steps + 1));
                    }
                }
                None => {
                    paths.insert((new_y, new_x), current_steps + 1);
                    search_buffer.push_back((new_y, new_x, current_steps + 1));
                }
            }
        }
    }

    return paths;
}

fn print_grid(grid: &Vec<Vec<char>>, paths: &HashMap<Point, u32>) {
    // Print that grid baby
    for (y, row) in grid.iter().enumerate() {
        println!(
            "{}",
            row.into_iter()
                .enumerate()
                .map(|(x, a)| if paths.contains_key(&(y, x)) {
                    a.to_ascii_uppercase()
                } else {
                    *a
                })
                .collect::<String>()
        );
    }
}
