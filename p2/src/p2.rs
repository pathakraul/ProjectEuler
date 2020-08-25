fn evenfibonnaci(){
    let mut x = 1;
    let mut y = 2;
    let mut tmp = 0;
    let mut count = 2;
    while tmp < 4000000 {
        tmp = x + y;
        x = y;
        y = tmp;
        if tmp % 2 == 0{
            count += tmp;
        }
    }
    println!("{}", count);
}

fn main() {
    evenfibonnaci();
}
