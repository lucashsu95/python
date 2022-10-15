#1101 格雷碼
def f_change(Lvalue):
    if Lvalue == '0':
        return '1'
    else:
        return '0'
Llist = []
num = '000'
n = int(input())
for i in range(1,n+1):
    #print('-----------',i,'-----------')
    if i % 2 == 0:
        for j in range(len(num),0,-1):
            # print('>>>',num[j-1],j)
            if num[j-1] == '1':
                # print('!!')
                num = list(num)
                #print(num,num[j-2])
                num[j-2] = f_change(num[j-2])
                num = ''.join(num)
                break
            
    else:
        num = num[:-1] + f_change(num[-1])
    Llist.append(num)
for i in range(len(Llist)):
    

for i in range(len(Llist),0,-1):

# print(num,'end')
