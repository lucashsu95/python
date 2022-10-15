#510 費氏數列   
def fib(n):
    i =  0
    j = count = 1
    ary = []
    
    while count < n:
        i , j = j , i + j
        ary.append(i)
        count += 1
    return ary
while 1:
    try:

        Lstr = ''
        result = int(input())
        for i in fib(result):
            Lstr = Lstr + str(i) + ' '
        print(Lstr)
    except:
        break