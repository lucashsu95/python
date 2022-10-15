#校驗和
for aaa in range(int(input())):
    a = input().split()
    data = []
    for i in range(0,20,2):
        data.append(int(a[i]+a[i+1],16))
    x = hex(sum(data))[2:]

    ans = int(x[:len(x)-4],16)+int(x[len(x)-4:],16)
    ans = bin(ans)[2:]
    ans = ans.rjust(16,'0')
    ans1 = ''
    for i in ans:
        if i=='1':
            ans1+='0'
        else:
            ans1+='1'
    ans2= hex(int(ans1,2))[2:]
    print(ans2.rjust(4,'0'))