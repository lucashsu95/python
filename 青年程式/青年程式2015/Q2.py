#題目 2： 網路位址問題
data = input().split(' / ')
print(data)
Lip = data[0].split('.')
Lnum = 32 - int(data[1])
Lright = ''
for i in range(int(data[1])):
    Lright += '1'
for j in range(Lnum):
    Lright += '0'


for i in range(len(Lip)):
    Lip[i] = f'{bin(int(Lip[i]))[2:]:0>8s}'
    

for i in range(len(Lright)):
    
print(Lip)
