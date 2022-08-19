#IMD2020［問題 1］非遞減字串
while 1:
    try :
        ary = []
        data = input()
        Lsum = 0
        for i in range(1,len(data)):
            if data[i-1] <= data[i]:
                Lsum += 1
            else:
                Lsum = 0
            ary.append(Lsum+1)
        print(max(ary))
    except:
        break