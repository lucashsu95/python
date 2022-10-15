for _ in range(int(input())):
    start_a,end_a,start_b,end_b,start_m,end_m = list(map(int,input().split()))
    Lcount = 0
    for a in range(start_a,end_a+1):
        for b in range(start_b,end_b+1):
            for m in range(start_m,end_m+1):
                if (a+b) % m == (a-b) % m:
                    Lcount += 1
    print(Lcount)
                
