Lnum = 10
Lary = [1,5,10,50]

for i in range(4):
    #1元
    if Lary[i] == 1:
        Lsum = Lnum // Lary[i]
        print(f'{Lary[i]} * {Lsum} = {Lnum} 找0元')
    #5元
    if Lary[i] == 5:
        Lsum = Lnum // Lary[i]
        for k in range(1,Lsum+1):
            Lsum = Lnum // Lary[i] * k
            print(f'{Lary[i-1]} * {Lnum-Lary[i]*k} + {Lary[i]} * {k} = {Lnum} 找0元')
        Lsum = Lnum // Lary[i]
        print(f"{Lary[i]} * {Lsum+1} = {Lary[i]*(Lsum+1)} 找{Lary[i]*(Lsum+1)-Lnum}元")
    
    #10元
    if Lary[i] == 10:
        Lsum = Lnum // Lary[i]
        for k in range(1,Lsum+1):
            Lsum = Lnum // Lary[i] * k
            print(f'{Lary[i-3]} * {Lnum-Lary[i]*k} + {Lary[i]} * {k} = {Lnum} 找0元')
            
        Lsum = Lnum // Lary[i]
        for k in range(1,Lsum+1):
            Lsum = Lnum // Lary[i] * k
            print(f'{Lary[i-2]} * {(Lnum-Lary[i]*k)//Lary[i-2]} + {Lary[i]} * {k} = {Lnum} 找{Lary[i]*k+Lary[i-2]*(Lnum-Lary[i]*k)//Lary[i-1]-Lnum}元')
        
        Lsum = Lnum // Lary[i]
        print(f"{Lary[i]} * {Lsum+1} = {Lary[i]*(Lsum+1)} 找{Lary[i]*(Lsum+1)-Lnum}元")
    
    #50元
    if Lary[i] == 50:
        Lsum = Lnum // Lary[i]
        for k in range(1,Lsum+1):
            Lsum = Lnum // Lary[i] * k
            print(f'{Lary[i-3]} * {Lnum-Lary[i]*k} + {Lary[i]} * {k} = {Lnum} 找0元')
        for k in range(1,Lsum+1):
            Lsum = Lnum // Lary[i] * k
            print(f'{Lary[i-2]} * {Lnum-Lary[i]*k} + {Lary[i]} * {k} = {Lnum} 找{Lary[i]*k+Lary[i-2]*(Lnum-Lary[i]*k)-Lnum}元')
        
        Lsum = Lnum // Lary[i]
        print(f"{Lary[i]} * {Lsum+1} = {Lary[i]*(Lsum+1)} 找{Lary[i]*(Lsum+1)-Lnum}元")
#m42