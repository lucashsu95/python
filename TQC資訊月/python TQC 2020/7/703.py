#703 數組條件判斷
data = input()
ary = []
while data != 'end':
    ary.append(data)
    data = input()
Ltuple = tuple(ary)
print(Ltuple)
print(Ltuple[:len(Ltuple)//2])
print(Ltuple[len(Ltuple)//2:])