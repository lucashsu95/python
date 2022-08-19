#TL001 兩個字串是否相同
str1 = input().split()
str2 = input().split()
str1 = ''.join(str1)
str2 = ''.join(str2)
if str1 == str2:
    print('True')
else:
    print("False")