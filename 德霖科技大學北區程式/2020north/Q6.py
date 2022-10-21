num10 = int(input())
num2 = f'{num10:b}'
Lcount = 0
for i in num2:
    if i == '1':
        Lcount += 1
print(Lcount)

#3m