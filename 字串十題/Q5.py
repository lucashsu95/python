#第五題 字串
import sys

for line in sys.stdin.read().splitlines():

    Lresult = "F"

    if len(line) >= 5 and line.replace(".","").isdigit():
        
        if line.count(".") == 0:
            Lresult = "T"

        if line.count(".") == 1 and line[-1] != ".":
            Lresult = "T"
            
    print(Lresult)