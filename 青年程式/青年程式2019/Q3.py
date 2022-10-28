#題目 3：排序轉換問題 (10%) 
Lstr = list(input())
print(Lstr)

def fun(i,j):
    print(Lstr)
    for i in range(i,j):
        if Lstr[i] == '*' or Lstr[i] == '/':
            Lstr[i-1] += Lstr[i+1] + Lstr[i]
            Lstr.pop(i+1)
            Lstr.pop(i)
            
            break
    
    for i in range(i,j):
        if Lstr[i] == '+' or Lstr[i] == '-':
            Lstr[i-1] += Lstr[i+1] + Lstr[i]
            Lstr.pop(i+1)
            Lstr.pop(i)
            break
    if  '(' in Lstr:
        Lstr.pop(i)
        Lstr.pop(i-2)
    #print('i:',i)
    print(Lstr)
    return Lstr

if '(' in Lstr:
    while 1:
        for i in range(len(Lstr)):
            print(i)
            if Lstr[i] == ')':
                for j in range(i,-1,-1):
                    if Lstr[j] == '(':
                        Lstr = fun(j,i-1)
                        print(Lstr)
                        break
            if len(Lstr) == i+1:
                break
        if '(' not in Lstr:
            break



while 1:
    for i in range(len(Lstr)):
        if Lstr[i] == '*' or Lstr[i] == '/':
            Lstr[i-1] += Lstr[i+1] + Lstr[i]
            Lstr.pop(i+1)
            Lstr.pop(i)
            break
    if len(Lstr) == i:
        break
while 1:        
    for i in range(len(Lstr)):
        if Lstr[i] == '+' or Lstr[i] == '-':
            Lstr[i-1] += Lstr[i+1] + Lstr[i]
            Lstr.pop(i+1)
            Lstr.pop(i)
            break
    if len(Lstr) == i:
        break
        
print(''.join(Lstr))
