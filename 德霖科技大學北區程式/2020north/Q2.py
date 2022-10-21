Lnum = int(input())
Lcount = [Lnum]
def fun(Lnum):
    global Lcount
    
    Lnum2 = list(str(Lnum ** 2))
    Lten = Lone = 0

    if len(Lnum2) == 1:
        Lten = '0'
        Lone = Lnum2[0]
    else:
        Lten = min(Lnum2)
        Lone = max(Lnum2)

    Lresult = int(Lten + Lone)

    print(f"{Lnum:<5d} {''.join(Lnum2):<5s}")

    if Lresult in Lcount:
        print(f'"{Lresult:<4d} {Lresult**2:<5d}')
        return
    else:
        Lcount.append(Lresult)
        fun(Lresult)


fun(Lnum)
#20m