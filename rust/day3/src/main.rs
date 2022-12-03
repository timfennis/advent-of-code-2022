use std::collections::HashSet;

use itertools::Itertools;

fn main() {
    let input = include_str!("../input");
    let dict = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let mut sum = 0;

    for line in input.lines() {
        let length = line.len() / 2;

        let fst_set: HashSet<char> = line[0..length].chars().collect();
        let snd_set: HashSet<char> = line[length..].chars().collect();

        for f in fst_set.intersection(&snd_set) {
            sum += dict.find(*f).unwrap() as i32;
        }
    }

    println!("Part 1: {sum}");

    let mut sum = 0;
    let groups = input.lines().chunks(3);

    for group in groups.into_iter() {
        let inters = group
            .map(|g| g.chars().collect::<HashSet<char>>())
            .fold(dict.chars().collect::<HashSet<char>>(), |total, set| {
                total.intersection(&set).map(|x| *x).collect()
            });

        for f in inters {
            sum += dict.find(f).unwrap() as i32;
        }
    }

    println!("Part 2: {sum}");
}
