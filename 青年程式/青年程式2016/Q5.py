#題目  5：明文/密文(Plaintext/Ciphertext)轉換問題  (15%)
Lary = 'j v k i x c p o m t f g d y h e s r z b l q n w u a'.split()
Ldict = {}
for i in range(1,27):
    Ldict[Lary[i-1]] = i
#print(Lary)
Ldatas = input().split()
if Ldatas[0].isdigit():
    Ldatas = list(map(int,Ldatas))
    for i in Ldatas:
        print(Lary[i-1],end='')
else:
    Lsum = 0
    for i in range(len(Ldatas)):
        Lsum += Ldict[Ldatas[i]]
    print(Lsum)

#12m