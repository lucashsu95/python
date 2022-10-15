def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return
    Lary.append(num)

num = int(input())
ans = [num]
Lary = []
while 1:
    Lmin = []
    for i in range(2,num):
        prime(i)
    for i in Lary:
        for j in Lary:        
            # print(f'{i} + {j} = {i+j}')
            if num == i+j:
                Lmin.append(abs(i-j))
    num = min(Lmin)
    ans.append(str(min(Lmin)))
    if num <= 2:
        break
Lstr = ''
for i in ans:

    Lstr += str(i) + ','
print(Lstr)