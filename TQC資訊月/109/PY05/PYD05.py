data = list(input())
Lcount = 0
for i in range(len(data)):
    if data[i] != "(" and data[i] != ")":
        data[i] = "="
    if data[i] == "(":
        Lcount += 1
Lcount //= 2
print(Lcount)
for _ in range(Lcount+1):
    for i in range(len(data)):
        if data[i] == '(':
            for j in range(i,len(data)):
                if data[j] == '(':
                    i = j
                if data[j] == ")":
                    data[i] = '*'
                    data[j] = '*'
                    break

for i in range(len(data)):
    if data[i] == "(" or data[i] == ')':
        data[i] = '?'
print(''.join(data))