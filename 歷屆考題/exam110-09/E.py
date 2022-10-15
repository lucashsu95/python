#費氏數列
for i in range(int(input())):
    m = int(input())
    fib = [0,1]
    if m >= 2:
        for j in range(2,m+1):
            fib.append(fib[j-1]+fib[j-2])
    print(fib[m])

