#606 二維串列行列數
def compute(rows,cols):
    for i in range(rows):
        for j in range(cols):
            print(f'{j-i:>3d}',end='')
        print()
rows = int(input())
cols = int(input())
compute(rows,cols)