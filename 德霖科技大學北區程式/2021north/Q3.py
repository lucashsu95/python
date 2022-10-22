#試題三(16 分)：密碼分析器
while 1:
    try:
        Lpassword = input()
        Lpassword2 = Lpassword.lower()
        AtoZ_ary = [chr(i) for i in range(97,123)]
        level = 0

        if len(Lpassword) >= 8:
            level += 1

        if Lpassword != Lpassword2:
            level += 1

        for i in Lpassword2:
            if i not in AtoZ_ary:
                level += 1
                break
        # print(level)

        if level == 3:print("This password is STRONG")
        if level == 2:print("This password is GOOD")
        if level == 1:print("This password is ACCEPTABLE")
        if level == 0:print("This password is WEAK")
    except:
        break
#13m