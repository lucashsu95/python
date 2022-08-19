#第十題 字串
import sys

for Lstr in sys.stdin.read().splitlines():

    Lresult = "F"

    B = Lstr.replace("+", "").replace("-", "").replace("*", "").replace("/", "")

    if len(Lstr) >= 3 and (B.isdigit()) and Lstr[0].isdigit() and Lstr[-1].isdigit() :

        Lresult = "T"

        for i in range(1,len(Lstr)):

            Ls2 ="+-*/"
            M = Ls2.find(Lstr[i-1])
            N = Ls2.find(Lstr[i])

            if (M >= 0 and N>=0):

                Lresult = "F"
                
    print(Lresult)