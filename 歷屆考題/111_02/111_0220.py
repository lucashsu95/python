Lstr = input()
Llist = list(map(int,Lstr))
Lsum = sum(Llist)
if Lsum % 10 != 0:
    print(Lstr + str(10 - Lsum % 10))
else:
    print(Lstr + '0')
