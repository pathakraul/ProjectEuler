use std::env::args;
use std::str::FromStr;

fn isprime(num: u64) -> bool {
    if num <=3 {
        return (num > 1)
    }
    else if num%2 == 0 || num%3 == 0 {
        return false
    }
    
    let mut k = 5;
    while k <= (num as f64).sqrt() as u64 {
        if num%k == 0 && num%(k+2) == 0 {
            return false;
        }
        k += 6;
    }
    true
}


fn main() {
    let mut num = 0; 
    for arg in args().skip(1) {
        num = u64::from_str(&arg).unwrap();
    }
    let ret = isprime(num);
    println!("{} is prime: {}", num, ret);
}
