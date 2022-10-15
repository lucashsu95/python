#904 資料計算
Lfile = open('in.txt','r')
name,height,weight = [],[],[]
for i in Lfile:
    data = i.split()
    name.append(data[0])
    height.append(int(data[1]))
    weight.append(int(data[2]))
    print(f'{data[0]} {data[1]} {data[2]}')
print(f'Average height: {"{:.2f}".format(sum(height)/len(height))}')
print(f'Average weight: {"{:.2f}".format(sum(weight)/len(weight))}')
print(f'The tallest is {name[height.index(max(height))]} with {"{:.2f}".format(max(height))}cm')
print(f'The heaviest is {name[weight.index(max(weight))]} with {"{:.2f}".format(max(weight))}kg')