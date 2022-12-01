use itertools::Itertools;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let groups: Vec<i32> = input
        .split("\n\n")
        .map(|group| group.split("\n").map(|cal| cal.parse::<i32>().unwrap()))
        .map(|g| g.sum())
        .sorted()
        .rev()
        .collect();

    let first = groups.first().unwrap();

    println!("Solution 1: {first}");

    let top_three: i32 = groups[0..3].iter().sum();

    println!("Solution 2: {top_three}");
}
