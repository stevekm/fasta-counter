use std::env;
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    println!("{:?}", filename);

    let reader = BufReader::new(File::open(filename).unwrap());
    let first_header;

    for line in reader.lines() {
        match line {
            Ok(l) => {
                // l.starts_with('#')
                // let ch = l.chars().next().unwrap();
                if l.starts_with('>') {
                    break
                }
            }
            Err(e) => {println!("error parsing line: {:?}", e)}
        }
    }
}