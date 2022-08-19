#IMD2020［問題 2］找重覆
import sys
for line in sys.stdin.read().splitlines():
    line = list(line)
    line2 = line.copy()
    for i in line2:
        if line.count(i) >= 2:
            line.remove(i)
    line = ''.join(line)
    print(line)
