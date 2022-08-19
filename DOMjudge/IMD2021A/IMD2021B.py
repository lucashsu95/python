#IMD2021 prob-剪刀石頭布
ary = ['Tie','I lost','I won']
import sys
for line in sys.stdin.read().splitlines():
    user,computer = list(map(int,line.split(' ')))
    if user == computer:
        print(ary[0])
    elif user == 0 and computer == 2:
        print(ary[2])
    elif user == 2 and computer == 0:
        print(ary[1])
    
    elif user > computer:
        print(ary[2])
    else:
        print(ary[1])

    