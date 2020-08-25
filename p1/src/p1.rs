fn multiples() {
    let mut count:u64 = 0;
    for i in 1..1000000 {
        if i % 3 == 0 {
            count+=i;
        }
        else if i % 5 == 0 {
            count+=i;
        }
    }

    println!("{}", count);
}

fn main() {
    multiples();
}
