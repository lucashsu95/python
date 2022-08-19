#第二題 字串
import sys

for line in sys.stdin.read().splitlines():
    if len(line) >= 2 and line[0] == line[-1]:
        print('T')
    else:
        print('F')