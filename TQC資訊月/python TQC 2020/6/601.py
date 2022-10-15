#601 偶數索引值加總
ary,Lsum = [],[]
Lcount = 0
while 1:
    try:
        data = int(input())
        if Lcount % 2 == 0:
            Lsum.append(data)
        Lcount += 1
        ary.append(data)
    except:
        break
for i in range(0,len(ary),3):
    print(f'{ary[i]:<3d}{ary[i+1]:<3d}{ary[i+2]:<3d}')
print(sum(Lsum))