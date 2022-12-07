use std::collections::HashMap;

use scan_fmt::scan_fmt;

fn main() {
    let input = include_str!("../input");

    let mut path: Vec<String> = vec![];
    let mut map: HashMap<String, u64> = HashMap::new();
    map.insert("/".to_string(), 0);

    for line in input.lines() {
        if let Ok(dir) = scan_fmt!(line, "$ cd {}", String) {
            match dir.as_str() {
                "/" => {
                    path.clear();
                }
                ".." => {
                    path.pop();
                }
                _ => {
                    path.push(dir);
                }
            }
        }
        if let Ok(dir) = scan_fmt!(line, "dir {}", String) {
            // The joining is kinda wonky because it prepends a / if there is only one element
            let key = format_path(
                &path
                    .iter()
                    .chain(vec![dir].iter())
                    .map(|i| i.to_owned())
                    .collect::<Vec<String>>(),
            );
            // let key = format_path();
            map.insert(key, 0);
        }
        if let Ok((size, _file_name)) = scan_fmt!(line, "{d} {}", u64, String) {
            let key = format_path(&path);
            *map.get_mut(&key).unwrap() += size;
            for i in 0..path.len() {
                let key = format_path(&path[0..i]);
                *map.get_mut(&key).unwrap() += size;
            }
            // dbg!((size, dir));
        }
    }

    let mut sum = 0;
    let mut min = std::u64::MAX;

    let total_required = 70000000u64 - 30000000;
    let total_in_use = *map.get("/").unwrap();
    let required = total_in_use - total_required;

    for (_, size) in map {
        if size < 100000 {
            sum += size;
        }

        if size > required && size < min {
            min = size
        } 
    }

    println!("Part 1: {sum}");
    println!("Part 2: {min}");
}

fn format_path(path: &[String]) -> String {
    match path.len() {
        0 => "/".to_string(),
        1 => format!("/{}", path.join("/")),
        _ => format!("/{}", path.join("/")),
    }
}
