#試題三(16 分)：密碼分析器
import sys
for line in sys.stdin.read().splitlines():
    Llevel = 0
    Lline = False
    LcapsA = False
    Lcapsa = False
    Lnumber = False
    Lorder = False

    if len(line) >= 8:
        Lline = True
    for i in line:
        if i.islower():
            Lcapsa = True
        elif i.isupper():
            LcapsA = True
        elif i.isdigit():
            Lnumber = True
        elif i == ' ':
            continue
        else:
            Lorder = True

    if Lline:
        Llevel += 1
    if Lcapsa and LcapsA:
        Llevel += 1
    if Lnumber or Lorder:
        Llevel += 1

    if Llevel == 3:
        print('Strong')
    elif Llevel == 2:
        print('Good')
    elif Llevel == 1:
        print("Acceptable")
    else:
        print('Weak')
    # print("Lline:",Lline)
    # print("Lcapsa,LcapsA:",Lcapsa,LcapsA)
    # print("Lnumber,Lorder:",Lnumber,Lorder)
    # print("Lline:",Lline)

    
        