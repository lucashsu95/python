while 1:
    try:
        n,c = map(int,input().split())
        np = []
        for i in range(1,n+1):
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                np.append(str(i))
        line = len(np)
        if c*2 >= line or c*2-1 >= line:
            start,end = 0,line

        elif line % 2 == 0:
            start = line//2-c
            end = start+(c*2)
            
        else:
            start = line//2-(c-1)
            end = start+(c*2-1)

        ans = ' '.join(np[start:end])
        print(f'{n} {c}: {ans}')
        
    except:
        break