#TA001 OX棋
def fun(num):
    for i in range(len(num),3):
        if num[i] == num[i+1] == num[i+2]:
            print(num[i])
            return True

    for i in range(3):
        if num[i] == num[i+3] == num[i+6]:
            print(num[i])
            return True
    
    return False


n = input().split()

if fun(n):
    pass
elif (n[0] == n[4] == n[8]) or (n[2] == n[4] == n[6]):
    print(n[0])
else:
    print('平手')



