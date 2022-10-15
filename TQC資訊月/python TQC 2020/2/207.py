#207 折扣方案
data = int(input())
if data >= 38000:
    print(data*0.7)
elif data >= 28000:
    print(data*0.8)
elif data >= 18000:
    print(data*0.9)
elif data >= 8000:
    print(data*9.5)
else:
    print(data)