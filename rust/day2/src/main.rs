use std::collections::HashMap;

fn main() {
    let input = std::fs::read_to_string("input").unwrap();

    let scores_1 = HashMap::from([
        ("A X", 3 + 1), ("A Y", 6 + 2), ("A Z", 0 + 3),
        ("B X", 0 + 1), ("B Y", 3 + 2), ("B Z", 6 + 3),
        ("C X", 6 + 1), ("C Y", 0 + 2), ("C Z", 3 + 3),
    ]);
    
    let scores_2 = HashMap::from([
        ("A X", 3 + 0), ("A Y", 1 + 3), ("A Z", 2 + 6),
        ("B X", 1 + 0), ("B Y", 2 + 3), ("B Z", 3 + 6),
        ("C X", 2 + 0), ("C Y", 3 + 3), ("C Z", 1 + 6),
    ]);

    let mut part_1_score = 0;
    let mut part_2_score = 0;

    for line in input.lines() {
       part_1_score += scores_1.get(line).unwrap();
       part_2_score += scores_2.get(line).unwrap();
    } 

    println!("Part 1: {part_1_score}\nPart 2: {part_2_score}");
}
