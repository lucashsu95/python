xy = [0,0]
Loption = list(input())

for i in Loption:
    if i == 'U':
        xy[0] += 1
    elif i == 'D':
        xy[0] -= 1
    elif i == 'L':
        xy[1] -= 1
    elif i == 'R':
        xy[1] += 1
if xy[0] == 0 and xy[1] == 0:
    print('Y')
else:
    print('N')
