#題目 8：明文/密文(Plaintext/Ciphertext)轉換問題 (10%)
Ldict_A = {}
Ldict_lower = {}
for i in range(65,90+1):
    Lvalue = i + 5
    if Lvalue > 90:
        Lvalue -= 26
    Ldict_A[chr(i)] = chr(Lvalue)
    if Lvalue+32 > 123:
        Lvalue += 32 - 26
    Ldict_lower[chr(i+32)] = chr(Lvalue+32)

# print(Ldict_A)
# print(Ldict_lower)
Lstr = list(input())
for i in range(len(Lstr)):
    if Lstr[i] == ' ':
        continue
    if Lstr[i] in Ldict_A.keys():
        Lstr[i] = Ldict_A[Lstr[i]]
    else:
        Lstr[i] = Ldict_lower[Lstr[i]]
print(''.join(Lstr))