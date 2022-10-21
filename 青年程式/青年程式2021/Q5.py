#張三的數學作業
Lout = open("out.txt",'w',encoding='utf-8')
for i in range(1,3):
    with open(f'in{i}.txt','r') as n:
        n = n.read()
        if len(n) > 50:
            print('輸入錯誤\n',file=Lout)
            
            
            continue
        n = int(eval(n))

        if len(str(n)) > 5:
            n = str(n)
            n = int(n[-5:])

        Lout.write(f"{str(n)}\n")
    Lout.write(f'\n')
    
    