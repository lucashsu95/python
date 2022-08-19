#第六題 字串
import sys

for line in sys.stdin.read().splitlines():

    Lresult = "F"

    if len(line) == 5 :

        Lresult = "T"
        
        for i in range(1,len(line)):
            if line[i-1] >= line[i]:

                Lresult = "F"

    print(Lresult)