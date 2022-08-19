#輸出最多出現次數的字母,並且輸出有幾次
for k in range(int(input())):
    Lstra,Lstrb = input().split()
    Lmax = 0
    Lmax_char = ''

    for i in range(len(Lstra)):
        Lnuma = 0
        Lnumb = 0
        
        for j in range(len(Lstra)):
            if Lstra[j] == Lstra[i]:
                Lnuma += 1

        for j in range(len(Lstrb)):
            if Lstrb[j] == Lstra[i]:
                Lnumb += 1
            
        if Lnuma + Lnumb > Lmax:

            Lmax = Lnuma + Lnumb
            Lmax_char = Lstra[i]

    print(Lmax_char)
    print(Lmax)