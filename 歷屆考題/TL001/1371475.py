#TL001 以遞升及遞減重組字串
data = input().split(' ')

ary = []

for i in range(len(data)):
    Lint = int(data[i])
    for j in data[i+1:]:
        if Lint >= int(j):
            Lint -= int(j)
            #print(Lint)
            break
    ary.append(Lint)
print(ary)
            
    
