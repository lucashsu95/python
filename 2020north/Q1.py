num1 = input()
num2 = input()
Lspace = str(len(num1) * 2)

print(f"{num1:>{Lspace}s}")
print(f"{'x '+num2:>{Lspace}s}")
print('-'*int(Lspace))

for i in range(len(num2)-1,0,-1):
    Lresult = str(int(num2[i]) * int(num1))
    if Lresult == '0':
        Lresult = '0' * len(num1)
    print(f'{Lresult:>{Lspace}s}')
    # print(Lresult)
    Lspace = str(int(Lspace) - 1)
#20m