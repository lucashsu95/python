#IMD2021 prob-同位元
while 1:
    try:
        data = input()
        if data == '0' :
            exit()
        data2 = bin(int(data))
        data2 = str(data2[2:])
        Lcount = data2.count('1')
        print(f'The parity of {data2} is {Lcount} (mod 2).')
    except:
        exit()