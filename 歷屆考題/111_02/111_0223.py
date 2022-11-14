Lstr = input()
AtoZ = [chr(i) for i in range(65,91)]
Lary = [AtoZ[i] * 2 if i < 8 else AtoZ[i]*3 for i in range(len(AtoZ))]
Lary = list(''.join(Lary))
for i in Lstr:
    Lary.remove(i)
if Lary != []:
    print(''.join(sorted(set(Lary))))
else:
    print('*')