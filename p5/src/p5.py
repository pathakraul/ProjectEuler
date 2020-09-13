
""" Brute Force Approach for divisibility by every number
div = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def smallestmultiple():
    count = len(div)
    for num in range(2520, 100000000, 10): 
        for i in div:
            if num%i:
                break
            elif num%i == 0:
                count = count-1
        if count == 0:
            print(f"{num}")
            break
        count = len(div)

def isdivisible(num):
    count = len(div)

    for i in div:
        if num%i:
            print(f"not divisible by {i}")
            break
        elif num%i == 0:
            count = count-1
    
    if count == 0:
        return True
    else:
        return False

smallestmultiple()
#print(isdivisible(9699690))
"""

def smallestmultiple():
    count = len(range(2,21))
    for num in range(2520, 1000000000, 10): 
        for div in range(2,21):
            if num%div:
                break;
            elif num%div == 0:
                count = count - 1
        if count == 0:
            print(f"{num} divisible evenly)")
            break
        count = len(range(2,21))


smallestmultiple()
