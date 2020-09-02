import math
import argparse

primeslist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def argumentparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help = "Number for testing")
    args = parser.parse_args()
    if args.number:
        return int(args.number)
    else:
        print("provide the number")

def checkprime(num):
    if num <= 3:
        return num > 1
    elif num % 2 == 0 or num % 3 == 0:
        return False

    k = 5
    while k <= math.sqrt(num):
        if num % k == 0 or num % (k+2) == 0:
            return False
        k += 6
    
    return True

factors = []
def primefactors(num):
    for i in range(2, num//2):
        while(num%i == 0):
            factors.append(i)
            num = num//i
    print(factors)


def largestprimefactor(num):
    for i in range(int(math.sqrt(num)), 2, -1):
        if num%i == 0:
            if checkprime(i):
                return i


if __name__ == '__main__':
    num = argumentparser()
    primefactors(num)
    #print(largestprimefactor(600851475143))
"""    primes = []
    for i in range(2, 200):
        ret = checkprime(i)
        if ret:
            primes.append(i)
        
    for i in range(len(primes)):
        print(primes[i])

    print(f"length of primes {len(primes)}") 
"""
