#109E迴文
def fun(data):
    if data == data[::-1]:
        print(data)
    else:
        result = int(data) + int(data[::-1])
        fun(str(result))
n = int(input())
for i in range(n):
    data = input()
    fun(data)