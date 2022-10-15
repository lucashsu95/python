#TL001 最多層的小括號
data = input()
a = 0
Lmax = 0
for i in data:
    if i == '(':
        a += 1
    elif i == ')':
        a -= 1
    if Lmax < a:
        Lmax = a
print(Lmax)
