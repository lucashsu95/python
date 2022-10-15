#110T找最⼤TEST-MAX
ary1,ary2 = [],[]
for _ in range(int(input())):
    data1,z,data2 = list(input())
    if data1 in ary2:
        if data1 in ary1:
            ary1.remove(data1)
    else:
        if data1 not in ary1:
            ary1.append(data1)
    if data2 in ary1:
        ary1.remove(data2)
    ary2.append(data2)

if ary1 == []:
    print('None')
else:
    print(','.join(sorted(ary1)))