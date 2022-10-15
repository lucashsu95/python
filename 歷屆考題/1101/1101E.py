#1101 E所有位數和
while 1:
    try:
        data = list(input())
        data = '+'.join(data)
        print(eval(data))
    except:
        break