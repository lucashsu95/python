Ln = int(input())
nation_dict = {}
name_list = []
for i in range(Ln):
    datas = input().split()
    nation = datas[0]
    name = ' '.join(datas[1:])
    if name not in name_list:
        name_list.append(name)
        if nation not in nation_dict.keys():
            nation_dict[nation] = 1
        else:
            nation_dict[nation] += 1

for i in sorted(nation_dict):
    print(i,nation_dict[i])