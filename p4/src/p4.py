def ispalindrome(num):
    ispalindrome = True
    num = str(num)
    numlen = len(num)
    for i in range(0, numlen//2):
        if num[i] == num[numlen-1-i]:
            pass
        else:
            ispalindrome = False
    
    return ispalindrome


if __name__ == '__main__':
    flag = False
    for i in range(998001, 10000, -1):
        if ispalindrome(i):
            for j in range(999, 100, -1):
                if i%j == 0:
                    if len(str(i//j)) == 3:
                        print(i, j)
                        flag=True
                        break
        if flag:
            break



