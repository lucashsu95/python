#阿拉伯數目字轉換國字大寫數字

n = int(input())
if n > 99999 or n < 0:
    print('超過範圍')
    exit()

ch = ['零','壹','貳','參','肆','伍','陸','柒','捌','玖']
ten = ["萬","仟","佰","拾"]
num = [10000,1000,100,10]
str = ''
for i in range(len(num)):
    n1 = n // num[i]
    n2 = n % num[i]

    if n1 > 0:
        str += ch[n1] + ten[i]
    else:
        if len(str) > 0:
            if str[-1] != "零":
                str += '零'
            
    n = n2
if n != 0:
    str += ch[n]
if str[-1] == "零":
    str = str[:len(str)-1] 
print(str)