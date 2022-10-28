Lstr = 'j v k i x c p o m t f g d y h e s r z b l q n w u a'
Lstr = Lstr.split()
Ldict = {}
j = 1
for i in Lstr:
    Ldict[j]=i
    j += 1
data = input().split()
if data[0] in Ldict.values():
    Lsum = 0
    while data != []:
        for i in range(1,len(Ldict)+1):
            if Ldict[i] in data:
                data.remove(Ldict[i])
                Lsum += i
    print(Lsum)
else:
    Lsum = ''
    for i in data:
        Lsum += Ldict[int(i)] + ' '
    print(Lsum)
