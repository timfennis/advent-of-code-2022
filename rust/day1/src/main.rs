fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let lines = input.split("\n");
    
    for line in lines {
        println!("{line}");
    }
}
