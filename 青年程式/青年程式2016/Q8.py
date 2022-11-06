#題目  8：馬雅日曆(Maya Calendar)轉換問題  (15%)
Haab = 'pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu, uayet'.split(', ')
Tzolkin = 'imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau'.split(', ')

month,day = input().split(', ')
SumDay = 0

for i in range(len(Haab)):
    if Haab[i] == month:
        break
    SumDay += 20
    

SumDay += int(day) + 1
idx = count = 0

for i in range(SumDay):
    idx += 1
    count += 1
    if idx >= len(Tzolkin):
        idx = 0
    if count >= 13:
        count = 0
print(Tzolkin[idx-1],count)
#18m