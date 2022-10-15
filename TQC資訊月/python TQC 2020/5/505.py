#505 依參數格式化輸出
def compute(Lchar,Lx,Ly):
    for i in range(Ly):
        for j in range(Lx):
            print(f'{Lchar:>2s}',end='')
        print()

while 1:
    try:
        Lchar = input()
        Lx = int(input())
        Ly = int(input())
        compute(Lchar,Lx,Ly)

    except:
        break