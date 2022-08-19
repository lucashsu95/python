#TL001 字串解碼
import sys
dict = {}
for i in range(1, 27):
    dict[str(i)] = chr(96+i)
#{'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}


for line in sys.stdin.read().splitlines():
    line = list(line)
    # print(line)
    ary = []
    Lstr = ''
    i = 0
    for i in range(len(line)):
        if line[i] != '#':
            ary.append(int(line[i]))
        else:
            if len(ary) != 0:
                ary.pop()
                ary.pop()
            ary.append(int(line[i-2]+line[i-1]))
    # print(ary)
    for j in range(len(ary)):
        Lstr += dict[str(ary[j])]
    print(Lstr)