#205 字元判斷
data = input()
if data.isalpha():
    print(data,'is an alphabet.')
elif data.isdigit():
    print(data,'is a number.')
else:
    print(data,'is a symbol.')