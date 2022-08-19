#第九題 字串
import sys

for Lstr in sys.stdin.read().splitlines():

    Lresult = "F"

    B = Lstr.replace("(", "").replace(")", "")

    if len(Lstr) >= 6 and (B.isdigit() or B == "") and Lstr.count("(")>=1 and  Lstr.count("(")==Lstr.count(")"):

        Lresult = "T"
        N = 0
        for i in range(0,len(Lstr)):

            if Lstr[i] == "(" :
                N+=1
            if Lstr[i] == ")" :
                N-=1

            if N<0:
                Lresult = "F"
                
    print(Lresult)