#106B羅馬數字
Ldict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
n = int(input())
for i in range(n):
    Lstr = input()
    Lsum = Ldict[Lstr[0]] #ans
    Lstr2 = Ldict[Lstr[0]]#if判斷

    for i in range(1,len(Lstr)):
        
        if Lstr2 >= Ldict[Lstr[i]]:
            Lstr2 = Ldict[Lstr[i]]
        else: 
            Lstr2 = Ldict[Lstr[i]] - Lstr2 - Lstr2

        Lsum += Lstr2

    print(Lsum)