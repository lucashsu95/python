#110T 幾A幾BTEST-AB
n = int(input())
for _ in range(n):
    data1,data2 = input().split(', ')
    a = b = 0
    ary1,ary2 = [],[]
    for i,j in zip(data1,data2):
        if i == j :
            a += 1
        else:
            ary1.append(i)
            ary2.append(j)
    for i in ary1:
        if i in ary2:
            b += 1
            ary2.remove(i)
    print(f'{a}A{b}B')
        
