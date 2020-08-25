def evenfibonnaci():
    x = 1
    y = 2
    tmp = 0
    #print(x)
    #print(y)
    count = 2
    while tmp < 4000000:
        tmp = x + y
        x = y
        y = tmp
        #print(tmp)
        if tmp % 2 == 0:
            count += tmp
    print(count)

evenfibonnaci()
