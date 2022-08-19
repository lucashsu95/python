#第一題 字串
import sys

for line in sys.stdin.read().splitlines():
    if len(line) == 5 and line.isdigit():
        print('Ture')
    else:
        print('False')