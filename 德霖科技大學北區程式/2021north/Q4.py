#試題四(18 分)：算式檢查
n = int(input())
for i in range(n):
    Lsum = 0
    a = list(map(str,input()))

    for j in range(len(a)):
        if a[j] == "]":
            Lsum -= 1
        elif a[j] == ')':
            Lsum -= 1
        elif a[j] == "(":
            Lsum += 1
        elif a[j] == "[":
            Lsum += 1
        else:
            pass
    if Lsum == 0:
        print("Valid")
    else:
        print('Try again')
        
