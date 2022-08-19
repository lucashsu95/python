#109D數字相乘
n = int(input())
for _ in range(n):
    data = int(input())
    Lresult = ''
    for i in range(9,1,-1):
        while data % i == 0:
            Lresult += str(i)
            data /= i
    if data <= 1 and Lresult != []:
        print(Lresult[::-1])
    else:
        print(-1)