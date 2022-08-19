#TL001 兩個數字的漢明距離
num1,num2 = int(input()),int(input())
num1 = '{:>034s}'.format(bin(num1)[2:])
num2 = '{:>034s}'.format(bin(num2)[2:])

Lcount = 0
for i,j in zip(num1,num2):
    if i != j:
        Lcount += 1
print(Lcount)


