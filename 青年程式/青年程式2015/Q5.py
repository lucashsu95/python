#題目 5：檢查碼問題
alpha = [chr(i) for i in range(65,91)]

alpha.insert(0,'')
# print(alpha)
val = list(input())
# print(val)
val[0] = alpha.index(val[0])

if len(str(val[0])) == 1:
    val.insert(0,'0')

val = list(map(int,val))
end = val[-1]
val = val[:-1]
# print('val:',val)
num = [1,9,8,7,6,5,4,3,2,1]

if val[1] != 1 and val[1] != 2:
    print('無效')

for i in range(len(val)):
    val[i] *= num[i]
# print(val)
if sum(val) % 10 == end:
    print('有效')
else:
    print('無效')
