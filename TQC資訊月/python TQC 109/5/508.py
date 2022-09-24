#508 最大公因數
def compute(x, y):
    if y == 0:
        return x
    else:
        return compute(y, x % y)
x, y = eval(input())
print(compute(x, y))