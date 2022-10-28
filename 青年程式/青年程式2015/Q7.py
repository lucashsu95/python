Lnum = 370
i = 0
Lnum2 = list(Lnum)
while i < Lnum:
    print(Lnum)
    i += 1
    Lsum = 0
    for i in range(len(Lnum2)):
        Lsum += Lnum2[i] ** i
    if Lsum == Lnum or Lsum > Lnum:
        print(Lsum)
        break
    
