#107B井字棋
def check(L,num):
    for i in range(0,7,3):
        if (L[i] == L[i+1] == L[i+2] == num):
            # print(L[i],L[i+1],L[i+2])
            print(num)
            return True
    for j in range(0,3):
        if (L[j] == L[j+3] == L[j+6] == num):
            # print(L[j],L[j+3],L[j+6])
            print(num)
            return True
    return False
        
n = int(input())
for _ in range(n):
    L = ''
    for _ in range(3):
        L += input()
    L = list(map(int,L))
    
    if check(L,1):
        pass
    elif check(L,2):
        pass
    elif (L[0] == L[4] == L[8] == 1) or (L[2] == L[4] == L[6] == 1):
        print(1)
    elif (L[0] == L[4] == L[8] == 2) or (L[2] == L[4] == L[6] == 2):
        print(2)
    else:
        print('3')