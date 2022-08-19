#第八題 字串
import sys

for Lstr in sys.stdin.read().splitlines():
    Lresult = "F"
    if len(Lstr) >= 2 :
        Lresult = "T"
        Lswitch = "a"
        for i in range(1,len(Lstr)):

            if Lswitch == "a":
                if Lstr[i-1] > Lstr[i]:
                    Lswitch = "d"
            else:
                if Lstr[i-1] < Lstr[i]:
                    Lresult = "F"

    print(Lresult)