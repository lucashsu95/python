#103F費氏數列
n = int(input())

fib = [1, 2]
while fib[-1] < 10000:
    fib.append(fib[-1] + fib[-2])

fib = fib[:-1]
fib = fib[::-1]

def f(x):
    output = ''
    for i in fib:
        if x >= i:
            x -= i
            output += '1'
        elif output != '':
            output += '0'

    return output


for _ in range(n):
    x = int(input())
    y = f(x)
    print(f'{x}={y}')

    # z = sum([fib[len(fib)-len(y)+i] for i in range(len(y)) if y[i] == '1'])
    # print(x == z)
