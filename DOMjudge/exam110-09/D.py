#質數
for i in range(int(input())):
    a = int(input())
    bool = True
    for j in range(2,int(a/2)+1):
        if a % j == 0:
            bool = False
            break
    if bool:
        print('T')
    else:
        print('F')