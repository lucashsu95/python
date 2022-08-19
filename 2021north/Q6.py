#裂解之數
import sys
for line in sys.stdin.read().splitlines():
    n = 0
    t1 = 0
    a,b = list(map(int,line.split( )))
    for i in range(a,b+1):
    
        for j in range(2,i):

            #print("i:",i)
            #print("j:",j)
            t1 = j
            while i > t1:
                t1 *= j


            #print("t1:",t1)
            #print("_____")
            if t1 == i:
                n += 1
                break
    print(n)