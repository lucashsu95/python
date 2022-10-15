#809密碼規則
password = input()
if len(password) <= 7 or password.isalnum() or password.isdigit() or password.islower():
    print('Invalid password')
else:
    print('Valid password')