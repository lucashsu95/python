#邏輯炸彈!
for i in range(int(input())):
    a = input()
    num = 0
    for j in a:
        if j == "(":
            num += 1
        if j == ")":
            num -= 1
        if num < 0:
            break
    if num == 0 :
        print("T")
    else:
        print("F")