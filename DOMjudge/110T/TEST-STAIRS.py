#110T印樓梯STAIRS
n = int(input())
count = ' '
sum = 0
cut = 0
while 1:
    for j in range(n):
        print(count*sum+'*')
    cut += 1
    if cut == n:
        break
    for k in range(n+1):
        if k == n:
            print('*')
        else:
            if k == 0:
                print(count*sum,end='')
            print('*',end='')
    cut+=1
    if cut == n:
        break
    sum += n