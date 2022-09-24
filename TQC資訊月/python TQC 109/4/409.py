#409 得票數計算
Nami = Chopper = null = 0
for i in range(5):
    user = int(input())
    if user == 1:
        Nami += 1
    elif user == 2:
        Chopper += 1
    else:
        null += 1
    print(f'Total votes of No.1: Nami =  {Nami}')
    print(f'Total votes of No.2: Chopper =  {Chopper}')
    print(f'Total null votes =  {null}')

if Nami > Chopper:
    won = 'No.1 Nami'
else:
    won = 'No.2 Chopper'
print(f'=>{won} won the election.')

