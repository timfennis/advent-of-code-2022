fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let mut groups: Vec<i32> = input
        .split("\n\n")
        .map(|group| group.split("\n").map(|cal| cal.parse::<i32>().unwrap()))
        .map(|g| g.sum())
        .collect();

    groups.sort_by(|a, b| b.partial_cmp(a).unwrap());

    let first = groups.first().unwrap();

    println!("Solution 1: {first}");

    let top_three: i32 = groups[0..3].iter().sum();

    println!("Solution 2: {top_three}");
}
