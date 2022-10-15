def bp(x, y, m):
    if y == 1:
        return x
    if y % 2 == 1:
        r = bp(x, y//2, m)
        return bp(x, 1, m) % m * (r % m) * (r % m)
    else:
        r = bp(x, y//2, m)
        return (r % m) * (r % m)


while True:
    try:
        x = int(input())
        y = int(input())
        m = int(input())
        print(bp(x, y, m) % m)
        span = input()

    except:
        break
