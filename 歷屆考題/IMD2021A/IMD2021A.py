#IMD2021 prob-五數有權重的相加(多列)
import sys
for line in sys.stdin.read().splitlines():
    a,b,c,d,e = list(map(int,line.split(' ')))
    print(56 * a + 24 * b + 14 * c + 6 * d + 2 * e)