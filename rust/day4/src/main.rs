fn main() {
    let input = include_str!("../input");

    let mut p1 = 0;
    let mut p2 = 0;

    for line in input.lines() {
        let split = line.split(|c| c == ',' || c == '-')
            .map(|s| s.parse::<u8>().unwrap())
            .collect::<Vec<u8>>();

        let n1 = split[0];
        let n2 = split[1];
        let n3 = split[2];
        let n4 = split[3];
        
        if n3 >= n1 && n4 <= n2 {
            p1 += 1;
        }
        else if n1 >= n3 && n2 <= n4 {
            p1 += 1;
        }

        if n2 >= n3 && n1 <= n4 {
            p2 += 1;
        }
    }

    println!("{}\n{}", p1, p2);
}
