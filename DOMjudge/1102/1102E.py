#字典
import sys

dict = {}

for item in sys.stdin.read().splitlines():
    data = item.split()
    if len(data) > 1:
        dict[data[1]] = data[0]
    elif len(data) > 0:
        if data[0] in dict.keys():
            print(dict[data[0]])
        else:
            print("eh")