#609 矩陣相加
ary,ary2 = [],[]
for i in range(4):
    ary.append(int(input()))
for j in range(4):
    ary2.append(int(input()))
print('Matrix 1')
print(f'**{ary[0]} {ary[1]}**')
print(f'**{ary[2]} {ary[3]}**')

print('Matrix 2')
print(f'**{ary2[0]} {ary2[1]}**')
print(f'**{ary2[2]} {ary2[3]}**')

print('Sum of 2 matrices')
print(f'**{ary[0]+ary2[0]} {ary[1]+ary2[1]}**')
print(f'**{ary[2]+ary2[2]} {ary[3]+ary2[3]}**')
