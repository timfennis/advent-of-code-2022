fn main() {
    let input = get_input();
    println!("part 1: {}", solve_part_one(&input));
    println!("part 2: {}", solve_part_two(&input));
}

fn solve_part_one(input: &Input) -> u32 {
    let mut solution = 0;

    for (offset, current_tree) in input.data.iter().enumerate() {
        let directions = [
            RayCast::new(input, Direction::Up, offset),
            RayCast::new(input, Direction::Down, offset),
            RayCast::new(input, Direction::Left, offset),
            RayCast::new(input, Direction::Right, offset),
        ];

        let is_visible = directions
            .into_iter()
            .any(|ray| ray.map(|(_, height)| height).all(|ot| ot < *current_tree));

        if is_visible {
            solution += 1;
        }
    }
    solution
}

fn solve_part_two(input: &Input) -> u32 {
    let mut best_score = 0;
    for (offset, current_tree) in input.data.iter().enumerate() {
        let directions = [
            RayCast::new(input, Direction::Up, offset),
            RayCast::new(input, Direction::Down, offset),
            RayCast::new(input, Direction::Left, offset),
            RayCast::new(input, Direction::Right, offset),
        ];

        let mut scores = vec![];
        for direction in directions {
            let mut score = 0;
            for (_, other_tree) in direction {
                score += 1;

                if other_tree >= *current_tree {
                    break;
                }
            }
            scores.push(score);
        }
        let score = scores.into_iter().product();

        if score >= best_score {
            best_score = score
        }
    }

    best_score
}

struct RayCast<'a> {
    input: &'a Input,
    direction: Direction,
    current_pos: usize,
}

impl<'a> RayCast<'a> {
    pub fn new(input: &'a Input, direction: Direction, pos: usize) -> Self {
        Self {
            input,
            direction,
            current_pos: pos,
        }
    }
}

enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Iterator for RayCast<'_> {
    type Item = (usize, u8);

    fn next(&mut self) -> Option<Self::Item> {
        let i_width = self.input.width as isize;
        let grid_size = (self.input.width * self.input.height) as isize;

        let offset = match self.direction {
            Direction::Up => (i_width).wrapping_neg(),
            Direction::Down => i_width,
            Direction::Left => -1,
            Direction::Right => 1,
        };

        let new_pos = (self.current_pos as isize) + offset;
        let current_row = (self.current_pos as isize).div_euclid(i_width);
        let new_row = new_pos.div_euclid(i_width);

        match self.direction {
            Direction::Left | Direction::Right if current_row != new_row => return None,
            Direction::Up | Direction::Down if new_pos < 0 || new_pos >= grid_size => return None,
            _ => {}
        }

        self.current_pos = new_pos as usize;

        self.input
            .data
            .get(self.current_pos)
            .map(|val| (self.current_pos, *val))
    }
}

struct Input {
    pub width: usize,
    pub height: usize,
    pub data: Vec<u8>,
}

fn get_input() -> Input {
    let input = include_str!("../input").lines();
    let width = input.clone().next().unwrap().len();
    let height = input.clone().collect::<Vec<_>>().len();

    Input {
        width,
        height,
        data: input
            .flat_map(|line| line.chars().map(|c| c.to_digit(10).unwrap() as u8))
            .collect::<Vec<_>>(),
    }
}

#[cfg(test)]
mod test {}
