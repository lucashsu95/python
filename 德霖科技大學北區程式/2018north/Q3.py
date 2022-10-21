Ln = int(input())
for i in [1,5,10,50]:
    if i == 1:
        print(f"1*{Ln}={Ln} 找0元")
    if i == 5:
        Lout = Ln // 5
        for j in range(1,Lout+1):
            if Ln - 5 * j == 0 : 
                print(f"5*{j}={Ln} 找0元")
                break
            print(f"1*{Ln-5*j}+5*{j}={Ln} 找0元")
        print(f"5*{Lout+1}={5*(Lout+1)} 找{5*(Lout+1)-Ln}元")
    if i == 10:
        Lout = Ln // 10
        for j in range(1,Lout+1):
            print(f"1*{Ln-10*j}+10*{j}={Ln} 找0元")
        for j in range(1,Lout+1):
            print(f"5*{1 if (Ln - 10*j)//5 == 0 else (Ln - 10*j)//5}+10*{j}={5*(1 if (Ln - 10*j)//5 == 0 else (Ln - 10*j)//5)+10*j} 找{(5*(1 if (Ln - 10*j)//5 == 0 else (Ln - 10*j)//5)+10*j) - Ln}元")
        print(f"10*{Lout+1}={10*(Lout+1)} 找{10*(Lout+1)-Ln}元")
    if i == 50:
        print(f"50*1=50 找{50-Ln}元")
#40m