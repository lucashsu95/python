Lstr = input()
Lstr2 = input()
Lans = ''

for i,j in zip(Lstr,Lstr2):
    Lans += i + j
if len(Lstr) < len(Lstr2):
    Lstr,Lstr2 = Lstr2,Lstr
    Lans += Lstr[len(Lstr2):]
elif len(Lstr) > len(Lstr2):
    Lans += Lstr[len(Lstr2):]
print(Lans)