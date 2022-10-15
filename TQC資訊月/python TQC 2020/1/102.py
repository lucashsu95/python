#102 浮點數格式化輸出
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

print(f'|{num1:>7.2f} {num2:>7.2f}|')
print(f'|{num3:>7.2f} {num4:>7.2f}|')

print(f'|{num1:<7.2f} {num2:<7.2f}|')
print(f'|{num3:<7.2f} {num4:<7.2f}|')