for i in range(int(input())):
    x1,y1,x2,y2 = list(map(int,input().split(' ')))

    result1 = abs(x1 - x2)
    result2 = abs(y1 - y2)  

    if result1 == result2 == 0:
        print(0)
    elif result1 == 0 or result2 == 0:
        print(1)
    elif result1 == result2:
        print(1)
    else:
        print(2)