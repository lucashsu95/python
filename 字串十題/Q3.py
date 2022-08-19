#第三題 字串
import sys


for line in sys.stdin.read().splitlines():
    a = int(len(line)/2)

    if len(line) >= 3 and len(line) % 2 == 1 and line[0] == line[a] and line[a] == line[-1]:
        print('T')
    else:
        print('F')