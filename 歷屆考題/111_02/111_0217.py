Lstr = input()
Lsum = 0
Lmax = 0
for i in Lstr:
    if i == '(':
        Lsum += 1
    elif i == ')':
        Lsum -= 1
    if Lmax < Lsum:
        Lmax = Lsum
print(Lmax)